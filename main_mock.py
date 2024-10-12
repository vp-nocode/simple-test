import requests
from config import TOKEN_OWM


def get_weather(city):
    api_key = TOKEN_OWM
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# city = 'London'
# weather_data = get_weather(city)
# print(weather_data)

def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# username = 'vp-nocode'
# user_github = get_github_user(username)
# print(user_github)
