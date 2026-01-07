> **Note**: This repository is a technical writing case study. I have taken an archived script and developed a professional-grade documentation suite to demonstrate API documentation, dependency management, and technical communication skills. [Read the full Case Study here](casestudy.md).

# Weather Reporter

Weather Reporter is a CLI-based python application that fetches real-time weather data for any city using the [OpenWeatherMap API](https://openweathermap.org/api).

## Contents
* [API Reference](api-reference.md) - Technical logic and data structures.
* [Contributing Guide](contributing.md) - How to enhance this project.
* [Requirements](requirements.txt) - Dependency list.
* [Case Study](casestudy.md) - Documentation refactor project overview.

## 🚀 Quick Start
1. **Get an API Key:** Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get your free API key.
2. **Configure the Script:** Open `main.py` and replace `"Your API key"` with your actual key.
3. **Install Dependencies:**
    ```bash
    pip install requests
    ```
4. **Run the App:**
    ```bash
    python main.py
    ```
5. **Input:** Enter the name of the city you want to check (e.g., "London").

## 📊 Features
* **Real-time Fetching:** Retrieves current weather descriptions (e.g., "clear sky", "light rain").
* **Temperature Conversion:** Automatically converts API data from Kelvin to Celsius.
* **Error Handling:** Basic validation for city names and API keys.

## Requirements

* **Python 3.x**
* **Requests Library:** Install it via terminal:
```bash
pip install requests
```



