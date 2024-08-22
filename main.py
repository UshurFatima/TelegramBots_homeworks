import asyncio
import logging
from bot_config import dp, bot, set_bot_commands, database

from handlers import (
    group_router,
    private_router
)


async def on_startup():
    print('Бот запущен')
    database.create_tables()


async def main():
    await set_bot_commands()
    dp.include_routers(private_router, group_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
