import asyncio
import logging
from bot_config import dp, bot

from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random_recipe import recipe_router
from dishes import dishes_router


async def main():
    dp.include_routers(start_router, myinfo_router, recipe_router, dishes_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
