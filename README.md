## WeatherBot AI: GPT-Powered Weather Information Tool 🌦️

This project is a **Streamlit-based web app** that uses **OpenAI's GPT-4o** and the **Visual Crossing Weather API** to provide weather information based on user input. The app leverages **function calling**, a cutting-edge feature of OpenAI's GPT-4, to interpret natural language queries and fetch relevant weather data.

![Demo Image](demo_image.png)

---

### Features 🌟

1. **Natural Language Query**: 
   - Users can type questions like *"What's the weather like in Karachi today?"*, and the app intelligently processes the query.
2. **GPT-4 Function Calling**:
   - OpenAI's GPT-4 interprets user input and determines the location for which weather data should be fetched.
3. **Real-Time Weather Data**:
   - Weather data is fetched from the **Visual Crossing Weather API**, providing accurate and up-to-date forecasts.
4. **Streamlit Interface**:
   - A clean, interactive UI built using Streamlit for seamless user experience.
5. **Error Handling**:
   - Robust error messages for invalid inputs or API issues.

---

### How It Works 🛠️

1. **User Query**:
   - The user types a question about the weather in natural language.
2. **GPT-4 Function Calling**:
   - GPT-4 analyzes the query and generates a function call with the location.
3. **Weather API Integration**:
   - The app uses the Visual Crossing Weather API to fetch weather data for the specified location.
4. **Response Display**:
   - The weather conditions and temperature are displayed on the Streamlit app interface.

---

### Technologies Used 🖥️

- **OpenAI GPT-4**: For natural language processing and function calling.
- **Visual Crossing Weather API**: For retrieving real-time weather data.
- **Streamlit**: For building an interactive and user-friendly web app interface.
- **Python**: For backend logic and API integration.
- **Requests Library**: To make HTTP requests to the weather API.
- **dotenv Library**: To manage API keys securely.

---

### API Details 🔑

#### 1. **OpenAI GPT-4 API**
- **Purpose**: Interprets natural language queries and identifies the location for weather data.
- **Feature Used**: Function Calling.
- **Example Function Call**:
  ```json
  {
    "name": "get_weather",
    "parameters": {
      "type": "object",
      "properties": {
        "location": {"type": "string"}
      }
    }
  }
  ```

#### 2. **Visual Crossing Weather API**
- **Purpose**: Fetches weather data based on the location provided.
- **Endpoint**: 
  ```
  https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast
  ```
- **Required Parameters**:
  - `locations`: Location for weather data.
  - `key`: API key for authentication.
  - `unitGroup`: Units for temperature (`metric` or `us`).
  - `contentType`: Response format (e.g., `json`).

---

### Installation & Setup 🛠️

#### Prerequisites:
- Python 3.8 or above.
- API keys for:
  - **OpenAI**: Sign up at [OpenAI](https://platform.openai.com/signup/).
  - **Visual Crossing Weather API**: Get your free key at [Visual Crossing](https://www.visualcrossing.com/).

#### Steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SyedAffan10/WeatherBot-AI.git
   cd WeatherBot-AI
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Place the KEYS**:
   - Place the keys in the code:
     ```
     OPENAI_API_KEY=your_openai_api_key
     VISUALCROSSING_API_KEY=your_visualcrossing_api_key
     ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   - Open the URL displayed in your terminal (e.g., `http://localhost:8501`) in your web browser.

---

### Folder Structure 📂

```
weatherbot-ai/
│
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .env                   # Environment variables (not tracked by Git)
└── LICENSE                # License file
```

---

### Example Usage 🚀

1. **Input**:
   - Type: *"What's the weather in Karachi today?"*
2. **Output**:
   - *"The weather in Karachi is clear with a temperature of 30°C."*

---

### Future Enhancements 🌐

- Add multi-day forecasts.
- Implement voice input for queries.
- Support multiple units (Celsius/Fahrenheit).
- Include additional weather details like humidity and wind speed.
