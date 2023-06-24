# almighty_weather

#NOTE: install 'request' by typing 'pip install requests' in the terminal of your IDE.

```
# Weather Forecast Tool

This is a command-line tool that fetches the current weather forecast for a given city using the Weatherbit API. It displays the temperature, temperature in Fahrenheit, weather description, humidity, and wind speed.

## Prerequisites

- Python 3.x
- requests library (can be installed using `pip install requests`)

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/your-username/weather-forecast-tool.git
   cd weather-forecast-tool
   ```

2. Install the required dependencies:
   ```
   pip install requests
   ```

3. Obtain an API key from Weatherbit API by signing up on their website: [Weatherbit API](https://www.weatherbit.io/).

4. Open the `weather_forecast.py` file and replace the `API_KEY` variable with your actual Weatherbit API key.

5. Run the tool:
   ```
   python weather_forecast.py
   ```

6. Follow the prompts and enter the city name for which you want to fetch the weather forecast. Enter "exit" to quit the program.

## Example Output

```
Enter the city name (or type 'exit' to quit): New York

Weather forecast for New York:
Temperature: 25.2°C
Temperature in Fahrenheit: 77.36°F
Description: Clear sky
Humidity: 78%
Wind Speed: 4.2 m/s

Enter the city name (or type 'exit' to quit): London

Weather forecast for London:
Temperature: 19.8°C
Temperature in Fahrenheit: 67.64°F
Description: Cloudy
Humidity: 62%
Wind Speed: 3.6 m/s

Enter the city name (or type 'exit' to quit): exit
Exiting the program...
```

## Contributions

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to customize the README file based on your specific project details and requirements. Make sure to replace "your-username" in the repository URL with your actual GitHub username.

Let me know if you have any further questions!
