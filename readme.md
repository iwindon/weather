# Weather Data Fetcher

This project fetches and prints weather data from the Ambient Weather Network API.

## Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```sh
pip install requests
```

### Setup
1. Clone the repository or download the source code.
2. Ensure you have a settings.py file in the same directory as weather.py with the following content:

```sh
# settings.py
AMBIENT_ENDPOINT = "https://rt.ambientweather.net/v1"
AMBIENT_APPLICATION_KEY = "your_application_key_here"
AMBIENT_API_KEY = "your_api_key_here"
```

### Usage

Run the `weather.py` script to fetch and print the weather data:
```sh
python weather.py
```

### Code Overview
#### Constants

* LAST_DATA: Key for the last data entry in the JSON response.
* TEMP_F: Key for the temperature in Fahrenheit.
* HUMIDITY: Key for the humidity percentage.
* WIND_SPEED: Key for the wind speed in mph.
* WIND_DIR: Key for the wind direction in degrees.
* RAIN_RATE: Key for the rain rate in inches per hour.
* PRESSURE: Key for the pressure in inches of mercury.
* UV_INDEX: Key for the UV index.

### Functions
* get_weather_data(): Fetches weather data from the Ambient Weather Network API.
* print_weather_data(data): Prints the weather data in a readable format.
### Error Handling
The script includes error handling to manage potential issues with the API response, such as missing keys or index errors.

### Example Output

```sh
The weather data at this moment is:
The temperature is 72.5 degrees Fahrenheit
The humidity is 55%
The wind speed is 5 mph
The wind direction is 180 degrees
The rain rate is 0.1 inches per hour
The pressure is 29.92 inches of mercury
The UV index is 5
```
### License
This project is licensed under the MIT License.
