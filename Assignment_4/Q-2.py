import requests

def getWeather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    final_url = f"{url}q={city}&appid={api_key}"

    try:
        response = requests.get(final_url)
        response.raise_for_status()
        data = response.json()
        Longitude = data["coord"]["lon"]
        Latitude = data["coord"]["lat"]
        Weather = data["weather"][0]["main"]
        Temperature = data["main"]["temp"]
        Humidity = data["main"]["humidity"]
        FeelLike = data["main"]["feels_like"]

        print(f"Weather Report For {city}: ")
        print(f"Coordinates:\n Longitude: {Longitude}\n Latitude: {Latitude}")
        print(f"Weather: {Weather}")
        print(f"Temperature: {Temperature}")
        print(f"Humidity: {Humidity}")
        print(f"Feels Like: {FeelLike}")
    except requests.exceptions.RequestException as e:
        print(f"Error Fetching the Data {e}")

city = input("Enter Your City Name to Check Weather Report: ")
getWeather(city,"55d93242421eda79dd568be9e661a7b7")
