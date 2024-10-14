import os

from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

WEATHER_TOKEN = os.getenv('API_WEATHER')

MESSAGE = {
    'help': (
                f'Данный бот отправляет погоду в заданном городе.\n'
                f'В качестве API используется ресурст OpenWeather https://openweathermap.org/'

    ),
    'no_city': 'Такого города не существует.\nПовторите запрос.'
}
