import os
import requests
import json
import streamlit as st
from openai import OpenAI

openai_api_key = "your_openai_api_key"
client = OpenAI(api_key=openai_api_key)

VISUALCROSSING_API_KEY="your_visualcrossing_api_key"

# Function to fetch weather data
def get_weather(location):
    """
    Fetch weather data for the given location using Visual Crossing Weather API.
    """
    api_key = os.getenv("VISUALCROSSING_API_KEY")
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast"
    params = {
        "locations": location,
        "aggregateHours": 24,
        "unitGroup": "metric",
        "shortColumnNames": "false",
        "contentType": "json",
        "key": VISUALCROSSING_API_KEY,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if "locations" not in data:
            return "Error: 'locations' key missing in the API response."

        # Extract weather details
        location_name = list(data["locations"].keys())[0]
        weather_data = data["locations"][location_name]["values"][0]
        temp = weather_data["temp"]
        conditions = weather_data["conditions"]

        return f"The weather in {location} is {conditions} with a temperature of {temp}°C."
    except Exception as e:
        return f"Error fetching weather data: {e}"

st.title("GPT Weather App 🌤️")
st.write("Enter a location below to get the weather information:")

user_query = st.text_input("Ask GPT about the weather", placeholder="What's the weather like in Karachi today?")

if st.button("Get Weather"):
    if user_query:
        with st.spinner("Processing your query..."):
            # Call GPT
            try:
                tools = [
                    {
                        "type": "function",
                        "function": {
                            "name": "get_weather",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "location": {"type": "string"},
                                },
                            },
                        },
                    }
                ]

                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": user_query}],
                    tools=tools,
                )

                # Extract tool call and execute
                tool_call = completion.choices[0].message.tool_calls[0]
                if tool_call.function.name == "get_weather":
                    arguments = json.loads(tool_call.function.arguments)
                    location = arguments["location"]
                    result = get_weather(location)
                    st.success("Weather fetched successfully!")
                    st.write(result)
                else:
                    st.error("GPT couldn't determine the location.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please enter a query.")
