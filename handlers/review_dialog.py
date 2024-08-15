from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import database


review_router = Router()


class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_router.callback_query(F.data == 'feedback')
async def give_review(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestaurantReview.name)
    await callback.message.answer('Как вас зовут?')


@review_router.message(RestaurantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestaurantReview.phone_number)
    await message.answer('Ваш номер телефона?')


@review_router.message(RestaurantReview.phone_number)
async def process_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(RestaurantReview.visit_date)
    await message.answer('В какой день вы посетили наш ресторан?'
                         ' (в формате ГГГГ-ММ-ДД)')


@review_router.message(RestaurantReview.visit_date)
async def process_date(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(RestaurantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Плохо')
            ],
            [
                types.KeyboardButton(text='Неудовлетворительно')
            ],
            [
                types.KeyboardButton(text='Удовлетворительно')
            ],
            [
                types.KeyboardButton(text='Хорошо')
            ],
            [
                types.KeyboardButton(text='Отлично')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Как бы вы оценили наши блюда?', reply_markup=kb)


@review_router.message(RestaurantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    food = message.text
    if food == 'Плохо':
        food = 1
    elif food == 'Неудовлетворительно':
        food = 2
    elif food == 'Удовлетворительно':
        food = 3
    elif food == 'Хорошо':
        food = 4
    elif food == 'Отлично':
        food = 5
    else:
        await message.answer('Пожалуйста, вводите только предложенные слова')
        return

    # if not food.isnumeric():
    #     await message.answer('Вводите только числа')
    #     return
    #
    # food = int(food)
    # if 5 < food or food < 1:
    #     await message.answer('Вводите числа от 1 до 5')
    #     return

    await state.update_data(food_rating=food)
    await state.set_state(RestaurantReview.cleanliness_rating)
    await message.answer('Как бы вы оценили чистоту нашего ресторана?')


@review_router.message(RestaurantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    clean = message.text
    if clean == 'Плохо':
        clean = 1
    elif clean == 'Неудовлетворительно':
        clean = 2
    elif clean == 'Удовлетворительно':
        clean = 3
    elif clean == 'Хорошо':
        clean = 4
    elif clean == 'Отлично':
        clean = 5
    else:
        await message.answer('Пожалуйста, вводите только предложенные слова')
        return

    # if not clean.isnumeric():
    #     await message.answer('Вводите только числа')
    #     return
    #
    # clean = int(clean)
    # if 5 < clean or clean < 1:
    #     await message.answer('Вводите числа от 1 до 5')
    #     return

    kb = types.ReplyKeyboardRemove()

    await state.update_data(cleanliness_rating=clean)
    await state.set_state(RestaurantReview.extra_comments)
    await message.answer('Какое впечатление у вас сложилось о ресторане?', reply_markup=kb)


@review_router.message(RestaurantReview.extra_comments)
async def process_comments(message: types.Message, state: FSMContext):
    await state.update_data(comments=message.text)

    await message.answer('Спасибо за ваш отзыв! Для нас очень важно ваше мнение!')
    data = await state.get_data()
    print(data)

    database.execute(query='''INSERT INTO reviews (name, phone_number, visit_date,
    food_rating, cleanliness_rating, comments) VALUES (?, ?, ?, ?, ?, ?)''',
                     params=(
                         data.get('name'),
                         data.get('phone_number'),
                         data.get('visit_date'),
                         data.get('food_rating'),
                         data.get('cleanliness_rating'),
                         data.get('comments')
                     ))

    await state.clear()
