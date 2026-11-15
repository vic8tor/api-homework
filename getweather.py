import requests


def get_weather():
    city = input()
    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "b5b794944b90d546720e9ad0c182cb5b"

    params = {

        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        weather = response.json()
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")

get_weather("")