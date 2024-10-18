import requests
import settings as settings

# Constants for JSON keys
LAST_DATA = 'lastData'
TEMP_F = 'tempf'
HUMIDITY = 'humidity'
WIND_SPEED = 'windspeedmph'
WIND_DIR = 'winddir'
RAIN_RATE = 'hourlyrainin'
PRESSURE = 'baromrelin'
UV_INDEX = 'uv'

# Function to get data from the AWN API
def get_weather_data():
    url = f"{settings.AMBIENT_ENDPOINT}/devices?applicationKey={settings.AMBIENT_APPLICATION_KEY}&apiKey={settings.AMBIENT_API_KEY}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

# Function to print weather data
def print_weather_data(data):
    try:
        weather = data[0][LAST_DATA]
        print("The weather data at this moment is:")
        print(f"The temperature is {weather[TEMP_F]} degrees Fahrenheit")
        print(f"The humidity is {weather[HUMIDITY]}%")
        print(f"The wind speed is {weather[WIND_SPEED]} mph")
        print(f"The wind direction is {weather[WIND_DIR]} degrees")
        print(f"The rain rate is {weather[RAIN_RATE]} inches per hour")
        print(f"The pressure is {weather[PRESSURE]} inches of mercury")
        print(f"The UV index is {weather[UV_INDEX]}")
    except (IndexError, KeyError) as e:
        print(f"Error accessing weather data: {e}")

# Main execution
if __name__ == "__main__":
    data = get_weather_data()
    print_weather_data(data)

