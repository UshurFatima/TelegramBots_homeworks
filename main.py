import asyncio
import logging
from bot_config import dp, bot, set_bot_commands, database

from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random_recipe import recipe_router
from handlers.dishes import dishes_router
from handlers.review_dialog import review_router


async def on_startup():
    print('Бот запущен')
    database.create_tables()


async def main():
    await set_bot_commands()
    dp.include_routers(start_router, myinfo_router,
                       recipe_router, review_router,
                       dishes_router)
<<<<<<< HEAD

    dp.startup.register(on_startup)
=======
>>>>>>> 0d66e6f0ab79e60c301b228f8e334d8d30d55f1f
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
