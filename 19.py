import json
# Load the JSON data from file
with open('weather_data.json') as f:
    weather_data = json.load(f)
# Extract the required weather data
current_temp = data['main']['temp']
humidity = weather_data ['main']['humidity']
weather_desc = weather_data ['weather'][0]['description']
# Display the weather data
print(f"Current temperature: {current_temp}°C")
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_desc}")
