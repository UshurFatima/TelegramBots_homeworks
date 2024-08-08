from aiogram import Router, types, F


dishes_router = Router()


@dishes_router.message(F.text == 'Супы')
async def soup_handler(message: types.Message):
    image = types.FSInputFile('menu_images/томатный.jpg')
    image_2 = types.FSInputFile('menu_images/минестроне.jpg')
    await message.answer_photo(photo=image, caption='Томатный суп с морепродуктами')
    await message.answer_photo(photo=image_2, caption='Суп минестроне')


@dishes_router.message(F.text == 'Вторые блюда')
async def main_dishes_handler(message: types.Message):
    image = types.FSInputFile('menu_images/маргарита.jpg')
    image_2 = types.FSInputFile('menu_images/пенне_арабьята.jpg')
    image_3 = types.FSInputFile('menu_images/ризотто.jpg')
    await message.answer_photo(photo=image, caption='Пицца Маргарита')
    await message.answer_photo(photo=image_2, caption='Пенне арабьята')
    await message.answer_photo(photo=image_3, caption='Ризотто с креветками')


@dishes_router.message(F.text == 'Десерты')
async def deserts_handler(message: types.Message):
    image = types.FSInputFile('menu_images/тирамису.jpg')
    image_2 = types.FSInputFile('menu_images/белый_лес.jpg')
    await message.answer_photo(photo=image, caption='Тирамису')
    await message.answer_photo(photo=image_2, caption='Торт белый лес')


@dishes_router.message(F.text == 'Лимонады')
async def lemonade_handler(message: types.Message):
    image = types.FSInputFile('menu_images/анман.jpg')
    image_2 = types.FSInputFile('menu_images/цитбаз.jpg')
    await message.answer_photo(photo=image, caption='Лимонад ананас-манго')
    await message.answer_photo(photo=image_2, caption='Лимонад цитрус-базилик')
