import math
import datetime
import requests

from bot import dispatcher, api_token, send
from aiogram.types import Message


# compass = ["Северный", "Северо-Восточный", "Восточный", "Юго-Восточный",
#            "Южный", "Юго-Западный", "Западный", "Северо-Западный"]

smiles = {
    "Clear": "\U00002600",
    "Clouds": "\U00002601",
    "Rain": "\U00002614",
    "Orizzle": "\U00002614",
    "Thunderstorm": "\U000026A1",
    "Snow": "\U0001F328",
    "Mist": "\U0001F32B",
}

compass = [
    "Северный",
    "Северо-Западный",
    "Западный",
    "Юго-Западный",
    "Южный",
    "Юго-Восточный",
    "Восточный",
    "Северо-Восточный",
]

@dispatcher.message_handler(commands=["start"])
async def start(message: Message):
    await message.reply("Bot is ready")
    await message.delete()


@dispatcher.message_handler()
async def getweather(message: Message):
    try:
        city = message.text
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={api_token}")
        data = response.json()

        description = data['weather'][0]
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_direction = compass[int((data['wind']['deg'] + 22.5) / 45)]
        wind_speed = data['wind']['speed']

        print(data['wind']['deg'])
        smile = smiles[description['main']] if description['main'] in smiles else ''

        await message.reply(f"{smile} {description['description'].capitalize()}, {temp}\u2103\n{humidity}% Влажность, {pressure} гПа\nСкорость ветра {wind_speed} км/ч\nНаправление ветра {wind_direction}")
    except:
        await send(message.chat.id, "Ошибка Сервера")