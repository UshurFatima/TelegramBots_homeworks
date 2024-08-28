from aiogram import Router, types, F
from bot_config import bot
from datetime import timedelta
from bot_config import database

group_router = Router()
group_router.message.filter(F.chat.type != 'private')
FORBIDDEN_WORDS = {'тупой', 'тупая', 'дура', 'лох', 'дурак', 'козел', 'полоумный', 'скотина'}


@group_router.message()
async def forbidden_words(message: types.Message):
    text = message.text
    for word in FORBIDDEN_WORDS:
        if word in text.lower():
            try:
                database.execute(query='''INSERT INTO warnings (user_id) VALUES (?)''',
                                 params=(message.from_user.id,))
            except:
                pass

            database.execute(query='''UPDATE warnings SET counter = counter + 1 WHERE user_id = ?''',
                             params=(message.from_user.id,))
            to_return = database.fetch(query='''SELECT counter FROM warnings WHERE user_id = ?''',
                                     params=(message.from_user.id, ))

            await message.answer(f'{message.from_user.first_name} не ругайся, твое '
                                 f'количество предупреждений достигло {to_return[0]["counter"]} раз')

            if to_return[0]['counter'] >= 10:
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=timedelta(seconds=60)
                )
            await message.delete()
            break
