import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

def get_weather(city):
    querystring = {"city": city}

    headers = {
        "X-RapidAPI-Key": "492511079dmshadeafacecd88f27p1f9a25jsn6ab2253e58c2",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()

        weather_data = response.json()
        
        # Extract the relevant weather information for the entered city
        city_weather = weather_data["data"][0]
        temperature = city_weather["temp"]
        description = city_weather["weather"]["description"]
        humidity = city_weather["rh"]
        wind_speed = city_weather["wind_spd"]

        # Print the weather information
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Temperature in Fahrenheit: {temperature * 33.8}°F")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print("Error occurred while retrieving weather data:", e)

# Loop to repeatedly ask for city names until the user chooses to exit
while True:
    city = input("Enter the city name (or type 'exit' to quit): ")
    
    if city.lower() == "exit":
        print("Exiting the program...")
        break
    
    get_weather(city)
    print()  # Print an empty line for better readability

print("Thank you for using the Weather Forecast Tool!")