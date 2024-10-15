import os

from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')

MESSAGE = {
    'help': (
                f'Данный бот отправляет погоду в заданном городе.\n'
                f'В качестве API используется ресурст OpenWeather https://openweathermap.org/'

    ),
    'no_city': 'Такого города <b>{city}</b> не существует.\nПовторите запрос.',
    'start': 'Привет {first_name} {last_name},\nЯ Weather_Api_Bot.',
    'repeat_input': 'Введи еще раз название города.',
    'bully': 'Вы издеваетесь!!!'

}
