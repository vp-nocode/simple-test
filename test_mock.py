import pytest
from main_mock import get_weather
from main_mock import get_github_user

def test_get_weather_success(mocker):
    mock_get = mocker.patch('main_mock.requests.get')
   # Create mock-answer for success request
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'broken clouds'}],
        'main': {'temp': 13.73}
    }


    city = 'London'
    weather_data = get_weather(city)

    assert weather_data == {
        'weather': [{'description': 'broken clouds'}],
        'main': {'temp': 13.73}
    }


def test_get_weather_error(mocker):
    mock_get = mocker.patch('main_mock.requests.get')
    mock_get.return_value.status_code = 404


    city = 'London'
    weather_data = get_weather(city)

    assert weather_data is None


def test_get_github_user_success(mocker):
    mock_get = mocker.patch('main_mock.requests.get')
   # Create mock-answer for success request
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nina'
    }


    user_data = get_github_user('nizavr')

    assert user_data == {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nina'
    }


def test_get_github_user_error(mocker):
   mock_get = mocker.patch('main_mock.requests.get')
   mock_get.return_value.status_code = 500

   user_data = get_github_user('cat')
   assert user_data == None
