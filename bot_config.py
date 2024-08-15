from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from database.database import Database


load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
database = Database('database.sqlite3')


async def set_bot_commands():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Начало работы бота'),
        types.BotCommand(command='myinfo', description='Информация о пользователе'),
        types.BotCommand(command='random_recipe', description='Случайный рецепт'),
        types.BotCommand(command='dishes', description='Список предлагаемых блюд')
    ])
