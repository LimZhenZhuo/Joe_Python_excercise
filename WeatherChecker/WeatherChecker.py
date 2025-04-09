import requests  # Import requests for API calls


def get_weather(city, api_key):
    # API endpoint for current weather data
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        "q": city,  # City name (e.g., "London")
        "appid": api_key,  # API key for authentication
        "units": "metric"  # Use metric units (Celsius)
    }

    try:
        # Send GET request to the API with timeout of 5 seconds
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()  # Raise error for HTTP status codes ≥400
        data = response.json()  # Parse JSON response into a dictionary

        # Check if the API returned an error (e.g., city not found)
        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return

        # Extract weather details from the response
        weather = data["weather"][0]["description"]  # Primary weather condition
        temp = data["main"]["temp"]  # Temperature in Celsius
        humidity = data["main"]["humidity"]  # Humidity percentage

        # Print formatted weather information
        print(f"City: {city}")
        print(f"Weather: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        # Handle network errors (e.g., timeout, connection failure)
        print(f"Request failed: {e}")


if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name (e.g., London): ")  # Prompt user for city
    get_weather(city, api_key)  # Execute the weather check