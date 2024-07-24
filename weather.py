from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Mumbai"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv('API_key')}&q={city}&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("Please input city name: ")

    # Check for emplty string and string with spaces
    if not bool(city.strip()):
        city = "Mumbai"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
