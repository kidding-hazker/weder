import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


bot_token = os.getenv('BOT_TOKEN')
api_token = os.getenv('API_TOKEN')


bot = Bot(token=bot_token)
dispatcher = Dispatcher(bot)

async def send(id, text: str):
    await bot.send_message(id, text)