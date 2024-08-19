from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


def dishes_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Супы'),
                KeyboardButton(text='Основные блюда'),
                KeyboardButton(text='Салаты')
            ],
            [
                KeyboardButton(text='Десерты'),
                KeyboardButton(text='Лимонады')
            ]
        ],
        resize_keyboard=True
    )
    return kb


def rating_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Плохо')
            ],
            [
                KeyboardButton(text='Неудовлетворительно')
            ],
            [
                KeyboardButton(text='Удовлетворительно')
            ],
            [
                KeyboardButton(text='Хорошо')
            ],
            [
                KeyboardButton(text='Отлично')
            ]
        ],
        resize_keyboard=True
    )
    return kb


def start_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='О ресторане', callback_data='about_us')
            ],
            [
                InlineKeyboardButton(text='Наш инстаграм', url='https://instagram.com/cyclone.bishkek'),
                InlineKeyboardButton(text='Наш сайт', url='https://cyclone.kg')
            ],
            [
                InlineKeyboardButton(text='Наш адрес и контакты', callback_data='info'),
            ],
            [
                InlineKeyboardButton(text='Вакансии', callback_data='vacancies'),
                InlineKeyboardButton(text='Оставить отзыв', callback_data='feedback')
            ]
        ]
    )
    return kb


def vacancies_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Обслуживающий персонал', callback_data='serving')
            ],
            [
                InlineKeyboardButton(text='Кухня', callback_data='kitchen')
            ],
            [
                InlineKeyboardButton(text='Администрация', callback_data='management')
            ]
        ]
    )
    return kb
