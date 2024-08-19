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
        await message.answer(f'Название: {dish[1]}\n'
                             f'Цена: {dish[2]} сом')


# @dishes_router.message(F.text.lower() == 'супы')
# async def soup_handler(message: types.Message):
#     image = types.FSInputFile('menu_images/томатный.jpg')
#     image_2 = types.FSInputFile('menu_images/минестроне.jpg')
#     kb = types.ReplyKeyboardRemove()
#     await message.answer_photo(photo=image, caption='Томатный суп с морепродуктами')
#     await message.answer_photo(photo=image_2, caption='Суп минестроне', reply_markup=kb)
#
#
# @dishes_router.message(F.text.lower() == 'основные блюда')
# async def main_dishes_handler(message: types.Message):
#     image = types.FSInputFile('menu_images/маргарита.jpg')
#     image_2 = types.FSInputFile('menu_images/пенне_арабьята.jpg')
#     image_3 = types.FSInputFile('menu_images/ризотто.jpg')
#     kb = types.ReplyKeyboardRemove()
#     await message.answer_photo(photo=image, caption='Пицца Маргарита')
#     await message.answer_photo(photo=image_2, caption='Пенне арабьята')
#     await message.answer_photo(photo=image_3, caption='Ризотто с креветками', reply_markup=kb)
#
#
# @dishes_router.message(F.text.lower() == 'десерты')
# async def deserts_handler(message: types.Message):
#     image = types.FSInputFile('menu_images/тирамису.jpg')
#     image_2 = types.FSInputFile('menu_images/белый_лес.jpg')
#     kb = types.ReplyKeyboardRemove()
#     await message.answer_photo(photo=image, caption='Тирамису')
#     await message.answer_photo(photo=image_2, caption='Торт белый лес', reply_markup=kb)
#
#
# @dishes_router.message(F.text.lower() == 'лимонады')
# async def lemonade_handler(message: types.Message):
#     image = types.FSInputFile('menu_images/анман.jpg')
#     image_2 = types.FSInputFile('menu_images/цитбаз.jpg')
#     kb = types.ReplyKeyboardRemove()
#     await message.answer_photo(photo=image, caption='Лимонад ананас-манго')
#     await message.answer_photo(photo=image_2, caption='Лимонад цитрус-базилик', reply_markup=kb)
#
#
# @dishes_router.message(F.text.lower() == 'салаты')
# async def lemonade_handler(message: types.Message):
#     image = types.FSInputFile('menu_images/капрезе.jpg')
#     image_2 = types.FSInputFile('menu_images/севиче.jpg')
#     kb = types.ReplyKeyboardRemove()
#     await message.answer_photo(photo=image, caption='Капрезе')
#     await message.answer_photo(photo=image_2, caption='Севиче из форели с авокадо', reply_markup=kb)
