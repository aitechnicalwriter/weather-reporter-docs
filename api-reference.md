# API Reference

This document provides a technical overview of the API integration used in the Weather Reporter script.

## Endpoint Details

The application interfaces with the **OpenWeatherMap Data API** to retrieve current weather conditions.

* **Base URL:** `http://api.openweathermap.org/data/2.5/weather`
* **Method:** `GET`
* **Authentication:** API Key (passed as `appid`)

## Request Parameters

The script constructs a request using the following parameters:

| Parameter | Type   | Description                                      |
| :---      | :---   | :---                                             |
| `appid`   | String | Required. Your unique OpenWeatherMap API key.     |
| `q`       | String | Required. The city name provided by user input.   |

## Data Extraction & Logic

The script processes a JSON response and extracts specific keys to display to the user.

### 1. Weather Description
* **Path:** `data["weather"][0]["description"]`
* **Description:** A human-readable summary of current conditions (e.g., "scattered clouds").

### 2. Temperature Conversion
The API returns the temperature in **Kelvin**. The script performs a manual conversion to **Celsius** before display.

**Formula:**
$$Celsius = Kelvin - 273.15$$

* **Path:** `data["main"]["temp"]`
* **Processing:** The result is rounded to two decimal places for readability.

## Error Handling

The script includes basic validation logic:
1.  **Status Code Check:** It verifies if the response code is `200` (OK).
2.  **Fallback:** If any other code is returned (e.g., `404` for invalid city or `401` for invalid API key), the script prints `"An error occurred."` to the console.