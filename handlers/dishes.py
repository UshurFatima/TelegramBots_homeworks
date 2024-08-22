from aiogram import Router, types, F
from aiogram.filters.command import Command

from keyboards import dishes_keyboard
from bot_config import database

dishes_router = Router()


@dishes_router.message(Command('dishes'))
async def dishes_handler(message: types.Message):
    await message.answer('Пожалуйста, выберите категорию блюд', reply_markup=dishes_keyboard())


categories = {'супы', 'основные блюда', 'десерты', 'салаты', 'лимонады'}


@dishes_router.message(F.text.lower().in_(categories))
async def categories_handler(message: types.Message):
    category = message.text
    print(category)
    kb = types.ReplyKeyboardRemove()
    menu = database.fetch(
        '''
        SELECT * FROM menu JOIN 
        food_categories ON menu.category_id = food_categories.id
        WHERE food_categories.name = ?
        ''',
        (category.capitalize(),)
    )
    if not menu:
        await message.answer(f'{category} нет в нашем меню')
        return

    await message.answer(f'Блюда категории {category}: ', reply_markup=kb)
    for dish in menu:
        image = types.FSInputFile(dish.get('image'))
        await message.answer_photo(photo=image, caption=
        f'Название: {dish.get('name')}\n'
        f'Цена: {dish.get('price')} сом')
