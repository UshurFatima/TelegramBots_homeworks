from aiogram import Router, types
from aiogram.filters.command import Command


myinfo_router = Router()


@myinfo_router.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    user_info = message.from_user
    await message.answer(f'Your first name: {user_info.first_name}  '
                         f'Your id: {user_info.id}  '
                         f'Your username: {user_info.username}')
