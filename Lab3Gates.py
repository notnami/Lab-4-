import requests

def weather(city):
    api_key = "Ye52c99220d9bc370bf25ee61ca9735b4"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    # Print the response for debugging
    print(data)  # Debugging line to check the entire API response

    if data["cod"] != "404":
        main = data.get("main")  # Use .get to avoid KeyError
        if main:  # Check if main exists
            weather_description = data["weather"][0]["description"]
            temp = main["temp"]
            print(f"Location: {data['name']}")
            print(f"Temperature: {temp}°C")
            print(f"Weather description: {weather_description}")
        else:
            print("Weather information is not available.")
    else:
        print("City Not Found")

# Taking user input
city = input("Enter the Name of City -> ")
weather(city)
print("\nHave a Nice Day :)")

