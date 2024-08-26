from aiogram import Router, types, F
from crawler.house_kg import HouseCrawler


house_router = Router()


@house_router.callback_query(F.data == 'houses')
async def show_houses(callback: types.CallbackQuery):
    crawler = HouseCrawler()
    links = crawler.get_links()
    for link in links:
        await callback.message.answer(link)
