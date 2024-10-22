from datetime import datetime

import requests


class Weather:

    def __init__(self, city, api_weather_token):
        self.__city = city
        self.__api_weather_token = api_weather_token

    def __weather_request(self,):
        requests_weather = requests.get(
            f'https://ru.api.openweathermap.org/data/2.5/weather?q={self.__city}&appid={self.__api_weather_token}&units=metric&lang=ru'
        )

        data = requests_weather.json()

        return (
            {
                'data': data,
                'status': data['cod']
            }
        )

    @property
    def get_weather(self,):
        return self.__weather_request()


class InfoMessage:

    def __init__(self, data):
        self.__data = data['data']

    @property
    def get_message(self):
        info_message = (
            f'Прогноз на: {datetime.fromtimestamp(self.__data['dt']).strftime("%d-%m-%Y %H:%M")}\n'
            f'Город: {self.__data['name']}\n'
            f'Состояние: {self.__data['weather'][0]['description']}\n'
            f'Температура: {int(self.__data['main']['temp'])}°C\n'
            f'Температура по ощущениям: {int(self.__data['main']['feels_like'])}°C\n'
            f'Влажность: {int(self.__data['main']['humidity'])}%\n'
            f'Скорость ветра: {round(self.__data['wind']['speed'], 1)}м/с\n'
            f'Давление: {int(self.__data['main']['pressure']/1.333)} мм рт.ст.\n'
            f'Восход: {datetime.fromtimestamp(self.__data['sys']['sunrise']).strftime("%H:%M")}\n'
            f'Закат: {datetime.fromtimestamp(self.__data['sys']['sunset']).strftime("%H:%M")}'
        )

        weather_icons = f'https://openweathermap.org/img/wn/{self.__data['weather'][0]['icon']}@2x.png'

        return (
            {
                'info_message': info_message,
                'weather_icons': weather_icons
            }
        )
