# API Reference: Weather Reporter

This section overviews the internal logic and the external API for the Weather Reporter CLI.

## External API Integration

To obtain current weather data we use the **Current Weather Data** endpoint of the [OpenWeatherMap API](https://openweathermap.org/api).

* **Base URL:** http://api.openweathermap.org/data/2.5/weather
* **Method:** GET
* **Authentication:** Using an API Key passed via the `appid` query parameter.

### Request Parameters
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `appid` | String | **Required.** Your OpenWeatherMap API Key. |
| `q` | String | **Required.** The name of the city you want to search (e.g., "London") |

---

## Functions Inside Main.py

The following functions have been defined inside `main.py` to manage the life cycle of the data from request to output.

### `get_weather(city, api_key)`
Get the raw weather data for a certain city.

* **Parameters:**
* `city (str)`: The name of the city that is being queried.
* `api_key (str)`: A valid OpenWeatherMap API Key.
* **Returns:**
* `dict`: A JSON formatted dictionary with information about the weather.
* `None`: Returns when the request failed (for example, 404 error or network timeout).

### `convert_kelvin_to_celsius(kelvin)`
Utility function to convert the temperature unit for better reading.

* **Logic:** The API has a default setting to return the temperature in Kelvin. To get it into Celsius we can simply apply the following conversion formula:
$$C = K - 273.15$$
* **Arguments:**
* `kelvin (float)`: The temperature that was provided by the API.
* **Returns:**
* `float`: Temperature in Celsius with a precision of two decimal places.

---

## Data Mapping

The script will take the most relevant parts from the big JSON response to show a simple view to the user.

| Display Name | Source Path | Example Value |
| :--- | :--- | :--- |
| **Condition** | `data["weather"][0]["description"]` | "clear sky" |
| **Temperature** | `data["main"]["temp"]` | 293.15 (Kelvin) |

---

## Error Handling

The application handles the following potential error states:

* **Invalid City:** In case of a 404 Not Found, the script will catch the exception and notify the user instead of crashing.
* **Network Problems:** With the help of `requests.exceptions.RequestException` we will be able to catch timeouts and/or connection problems in a graceful way.