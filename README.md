# Weather bot

## Тестовое задание

## Технологии:
* Python 3.12
* pyTelegramBotAPI 4.23


### Инструкция для запуска проекта:
- Клонируйте репозиторий
```
git clone git@github.com:Raa78/weather_bot.git
```
_или скачайте zip-архив_
```
https://github.com/Raa78/weather_bot/archive/refs/heads/main.zip
```

- Перейдите в папку с проектом
```
weather_bot
```
- Установите виртуальное окружение

Windows
```
python -m .venv venv
```

MacOS/Unix
```
python3 -m .venv venv
```
- Активируйте виртуальное окружение
  Windows \* Bash:

```
source .venv/Scripts/activate
```

    * Windows Shell:

```
.venv\Scripts\Activate.ps1
```

MacOS/Unix \* Bash/Zsh:

```
source .venv/bin/activate
```

- Установка зависимостей из файла requirements.txt
```
pip install -r requirements.txt
```

- В папке с проектом создайте файл .evn для хранения ключей:
```
TELEGRAM_TOKEN = # API токен от чат-бота
API_WEATHER = # API от погодного сервиса
```
В данном проекте использовался API погодного сервиса https://openweathermap.org/
