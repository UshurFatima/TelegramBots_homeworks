import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging
from random import choice

load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
user_id = []
counter = 0


@dp.message(Command('start'))
async def start_handler(message: types.Message):
    print(vars(message.from_user))
    global counter
    if message.from_user.id not in user_id:
        counter += 1
        user_id.append(message.from_user.id)
    await message.answer(f'Hello, {message.from_user.first_name}! '
                         f'Our bot already serves {counter} users')


@dp.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    user_info = message.from_user
    await message.answer(f'Your first name: {user_info.first_name}  '
                         f'Your id: {user_info.id}  '
                         f'Your username: {user_info.username}')


@dp.message(Command('random_recipe'))
async def recipe_handler(message: types.Message):
    recipes = [types.FSInputFile('recipes/chicken_hummus_bowl'),
               types.FSInputFile('recipes/couscous_salad'),
               types.FSInputFile('recipes/vegetarian_ramen')]
    await message.answer_document(choice(recipes))


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
