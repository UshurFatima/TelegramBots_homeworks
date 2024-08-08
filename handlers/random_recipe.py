from aiogram import Router, types
from aiogram.filters.command import Command
from random import choice


recipe_router = Router()


@recipe_router.message(Command('random_recipe'))
async def recipe_handler(message: types.Message):
    recipes = [types.FSInputFile('recipes/chicken_hummus_bowl'),
               types.FSInputFile('recipes/couscous_salad'),
               types.FSInputFile('recipes/vegetarian_ramen')]
    await message.answer_document(choice(recipes))
