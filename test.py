
# import re

# text = "  Нижний Но7456город"
# pattern = r'[A-Z][a-z][А-Я][а-я]'

# x = re.sub(pattern, "", text)

# print(x)

import requests
from datetime import datetime
from pprint import pprint

from constants import (
    WEATHER_TOKEN
)



def get_weather(city):

    requests_weather = requests.get(
        f'https://ru.api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric&lang=ru'
    )
    data = requests_weather.json()

    if data['cod'] == 200:
        print('Данные получены:')
        pprint(data)

        # current_date = datetime.fromtimestamp(data['dt'])
        # city = data['name']
        # current_weather = data['weather'][0]['description']  # состояние
        # current_temperature = int(data['main']['temp']) # температура
        # current_temperature_feels_like = int(data['main']['feels_like']) # температура по ощущению
        # current_humidity = int(data['main']['humidity'])  # влажность
        # current_wind = round(data['wind']['speed'], 1) # скорость ветра
        # current_pressure = int(data['main']['pressure']/1.333)  # давление
        # sunrise_time = datetime.fromtimestamp(data['sys']['sunrise'])  # время восхода
        # sunset_time = datetime.fromtimestamp(data['sys']['sunset'])  # время заката
        # weather_icon = data['weather'][0]['icon']

        # data_weather = (
        #     f'Дата: {current_date}\n'
        #     f'Город: {city}\nСостояние: {current_weather}\nТемпература: {current_temperature}\n'
        #     f'Влажность: {current_humidity}\nСкорость ветра: {current_wind}\n'
        #     f'Давление: {current_pressure}\nВосход: {sunrise_time}\nЗакат: {sunset_time}'
        # )

        # icons = f'https://openweathermap.org/img/wn/{weather_icon}@2x.png'

        # return (
        #     {
        #         'data_weather': data_weather,
        #         'icons': icons
        #     }
        # )
        return True

    else:
        return False


city = input('Введите город>>>')
get_weather(city)
