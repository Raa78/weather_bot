from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler


import requests
import telebot
from telebot import types

from constants import (
    TELEGRAM_TOKEN,
    HELP_HTML,
    WEATHER_TOKEN
)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
handler = RotatingFileHandler('weather_raa_api_bot_logger.log', maxBytes=50000000, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
API_TOKEN = TELEGRAM_TOKEN

bot = telebot.TeleBot(API_TOKEN)


def get_weather(city):

    requests_weather = requests.get(
        f'https://ru.api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric&lang=ru'
    )

    data = requests_weather.json()

    if data['cod'] == 200:
        # requests_weather = requests.get(
        #     f'https://ru.api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric&lang=ru'
        # )
        # data = requests_weather.json()

        current_date = datetime.fromtimestamp(data['dt'])
        city = data['name']
        current_weather = data['weather'][0]['description']  # состояние
        current_temperature = int(data['main']['temp']) # температура
        current_temperature_feels_like = int(data['main']['feels_like']) # температура по ощущению
        current_humidity = int(data['main']['humidity'])  # влажность
        current_wind = round(data['wind']['speed'], 1) # скорость ветра
        current_pressure = int(data['main']['pressure']/1.333)  # давление
        sunrise_time = datetime.fromtimestamp(data['sys']['sunrise'])  # время восхода
        sunset_time = datetime.fromtimestamp(data['sys']['sunset'])  # время заката
        weather_icon = data['weather'][0]['icon']

        icons = f'https://openweathermap.org/img/wn/{weather_icon}@2x.png'

        data_weather = (
            f'Дата: {current_date}\n'
            f'Город: {city}\nСостояние: {current_weather}\nТемпература: {current_temperature}\n'
            f'Температура по ощущениям: {current_temperature_feels_like}\n'
            f'Влажность: {current_humidity}\nСкорость ветра: {current_wind}\n'
            f'Давление: {current_pressure}\nВосход: {sunrise_time}\nЗакат: {sunset_time}'
        )

        return (
            {
                'data_weather': data_weather,
                'icons': icons
            }
        )

    else:
        message_error = f'Сбой в работе программы: {data['message']}'
        logger.error(message_error)
        return False


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message, res=False):

    logger.info(
        'Запущена функция send_welcome()'
    )

    # Создание клавиатуры
    # keyboard = types.ReplyKeyboardMarkup(row_width=2)
    # button1 = types.KeyboardButton('/help')
    # # button2 = types.KeyboardButton('Кнопка 2')
    # # button3 = types.KeyboardButton('Кнопка 3')
    # keyboard.add(button1)

    bot.send_message(
        message.chat.id,
        f'Привет {message.from_user.first_name}, I am Weather_Api_Bot.',
        # reply_markup=keyboard
    )


@bot.message_handler(commands=['help'])
def help_welcome(message):

    logger.info(
        'Запущена функция help_welcome()'
    )

    bot.send_message(message.chat.id, HELP_HTML, parse_mode='html')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def info_message(message):

    city_name =  message.text.strip().lower()

    weather_request = get_weather(city_name)

    if weather_request:
        weather_icons = weather_request['icons']

        bot.send_photo(message.chat.id, weather_icons)
        bot.send_message(message.chat.id, weather_request['data_weather'])
    else:

        report = 'Такого города не существует.\nПовторите запрос'

        bot.send_message(message.chat.id, report)



bot.infinity_polling()
