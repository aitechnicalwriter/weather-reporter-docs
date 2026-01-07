import requests

def get_weather(city, api_key):
    """
    Fetches real-time weather data for a specified city using the OpenWeatherMap API.

    Args:
        city (str): The name of the city to query.
        api_key (str): A valid OpenWeatherMap API key.

    Returns:
        dict: A JSON response containing weather details if successful, 
              or None if the request fails.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key
    }
    
    try:
        # Standard GET request to the OpenWeatherMap endpoint
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def convert_kelvin_to_celsius(kelvin):
    """
    Converts a temperature value from Kelvin to Celsius.

    Args:
        kelvin (float): The temperature in Kelvin.

    Returns:
        float: The temperature in Celsius rounded to two decimal places.
    """
    return round(kelvin - 273.15, 2)

def main():
    """
    Main entry point for the Weather Reporter CLI. 
    Handles user input, calls API logic, and formats output.
    """
    print("--- Weather Reporter ---")
    
    # Configuration: Replace with your actual OpenWeatherMap API key
    api_key = "Your_API_Key_Here"
    city = input("Enter city name: ")

    data = get_weather(city, api_key)

    if data:
        # Extracting specific data points from the JSON response
        description = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = convert_kelvin_to_celsius(temp_kelvin)

        print(f"\nWeather in {city.title()}:")
        print(f"Condition: {description}")
        print(f"Temperature: {temp_celsius}°C")
    else:
        print("Could not retrieve weather information. Please check the city name and your API key.")

if __name__ == "__main__":
    main()