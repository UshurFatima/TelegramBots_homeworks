import asyncio
import logging
from bot_config import dp, bot, set_bot_commands

from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random_recipe import recipe_router
from handlers.dishes import dishes_router
from handlers.review_dialog import review_router


async def main():
    await set_bot_commands()
    dp.include_routers(start_router, myinfo_router,
                       recipe_router, dishes_router,
                       review_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
