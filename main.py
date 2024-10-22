import logging
from logging.handlers import RotatingFileHandler

import telebot
from telebot import types

from constants import (
    MESSAGE,
    TELEGRAM_TOKEN,
    WEATHER_TOKEN,
)

from util import (
    InfoMessage,
    Weather
)

# loggers
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename='weather_basic_logger.log',
    filemode='a'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
handler = RotatingFileHandler(
    'weather_custom_logger.log',
    maxBytes=50000000,
    backupCount=5
)
handler.setFormatter(formatter)
logger.addHandler(handler)


# bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# keyboard
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
button_help = types.KeyboardButton(text='/help')
button_weather = types.KeyboardButton(text='Запросить погоду')
keyboard.add(button_weather, button_help).row()

count_error = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):

    logger.info(
        'Обращение к функции send_welcome()'
    )

    first_name = message.from_user.first_name
    last_name=message.from_user.last_name

    bot.send_message(
        message.chat.id,
        MESSAGE['start'].format(first_name=first_name, last_name=last_name),
        reply_markup=keyboard
    )


@bot.message_handler(commands=['help'])
def help_welcome(message):

    logger.info(
        'Обращение к функции help_welcome()'
    )

    bot.send_message(
        message.chat.id,
        MESSAGE['help'],
        parse_mode='html'
    )


@bot.message_handler(func=lambda message: message.text == 'Запросить погоду')
def weather_request(message):
        bot.send_message(message.chat.id, "Введи название города.")
        bot.register_next_step_handler(message, info_message)


def info_message(message):

    global count_error

    city_name =  message.text.strip().lower()

    weather_request = Weather(city_name, WEATHER_TOKEN)
    weather_request = weather_request.get_weather

    if weather_request['status'] == 200:

        weather_data = InfoMessage(weather_request)
        weather_data = weather_data.get_message

        bot.send_photo(message.chat.id, weather_data['weather_icons'])
        bot.send_message(
            message.chat.id,
            weather_data['info_message'],
            reply_markup=keyboard
        )
    else:
        report = MESSAGE['no_city'].format(city=message.text)

        count_error += 1

        if count_error < 3:

            bot.send_message(message.chat.id, report, parse_mode='html')

            bot.send_message(message.chat.id, MESSAGE['repeat_input'])
            bot.register_next_step_handler(message, info_message)
        else:
            count_error = 0
            bot.send_message(
                message.chat.id,
                MESSAGE['bully'],
                reply_markup=keyboard
            )


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    logger.info(
        'Бот запущен'
    )

    main()
