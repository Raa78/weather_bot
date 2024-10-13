import os

from dotenv import load_dotenv


load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

WEATHER_TOKEN = os.getenv('API_WEATHER')

HELP_HTML = """
<b>Help</b> Данный бот отправляет погоду в заданном городе.
"""

BUTTONS = ['Старт']
