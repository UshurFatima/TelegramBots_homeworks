from aiogram import Router, types, F
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='О ресторане', callback_data='about_us')
            ],
            [
                types.InlineKeyboardButton(text='Наш инстаграм', url='https://instagram.com/cyclone.bishkek'),
                types.InlineKeyboardButton(text='Наш сайт', url='https://cyclone.kg')
            ],
            [
                types.InlineKeyboardButton(text='Наш адрес и контакты', callback_data='info'),
            ],
            [
                types.InlineKeyboardButton(text='Вакансии', callback_data='vacancies'),
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='feedback')
             ]
        ]
    )
    await message.answer('Здравствуйте, я бот ресторана итальянской кухни Cyclone! '
                         'Чем я могу вам помочь?', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def aboutus_handler(callback: types.CallbackQuery):
    await callback.message.answer('Уже более 20 лет ресторан "Циклон" радует жителей '
                                  'и гостей города Бишкек изысканными блюдами итальянской кухнию '
                                  'Узнаваемые, но в то же время интересные блюда от нашего '
                                  'шеф-повара сделают ваш вечер незабываемым')


@start_router.callback_query(F.data == 'info')
async def info_handler(callback: types.CallbackQuery):
    await callback.message.answer('Адрес: Чуй 136 '
                                  'Номер телефона: +996700533633')


@start_router.callback_query(F.data == 'vacancies')
async def vacancies_handler(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Обслуживающий персонал', callback_data='serving')
            ],
            [
                types.InlineKeyboardButton(text='Кухня', callback_data='kitchen')
            ],
            [
                types.InlineKeyboardButton(text='Администрация', callback_data='management')
            ]
        ]
    )
    await callback.message.answer('Выберите интересующую вас должность', reply_markup=kb)


@start_router.callback_query(F.data == 'serving')
async def serving_handler(callback: types.CallbackQuery):
    await callback.message.answer('Свободна позиция официанта, для '
                                  'более подробной информации пишите на номер '
                                  '+996703456789')


@start_router.callback_query(F.data == 'kitchen')
async def kitchen_handler(callback: types.CallbackQuery):
    await callback.message.answer('К сожалению, на данный момент вакантных мест нет')


@start_router.callback_query(F.data == 'management')
async def management_handler(callback: types.CallbackQuery):
    await callback.message.answer('К сожалению, на данный момент вакантных мест нет')
