# Weather Reporter

Weather Reporter is a CLI-based python application that fetches real-time weather data for any city using the **OpenWeatherMap API**.

* **Real-time Fetching:** Retrieves current weather descriptions (e.g., "clear sky", "light rain").
* **Temperature Conversion:** Automatically converts API data from Kelvin to Celsius for better readability.
* **Error Handling:** Basic check to notify the user if the request fails (e.g., invalid city name or API key issues).

## Quick Start
1.  **Get an API Key:** Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get your free API key.
2.  **Configure the Script:** Open `main.py` and replace `"Your API key"` with your actual key.
3.  **Install Dependencies:**
    ```bash
    pip install requests
    ```
4.  **Run the App:**
    ```bash
    python main.py
    ```
5. **Input:** Enter the name of the city you want to check (e.g., "London").

## Requirements
* **Python 3.x**
* **Requests Library** (>= 2.31.0)

## Requirements

* **Python 3.x**
* **Requests Library:** Install it via terminal:
```bash
pip install requests
```



