from aiogram import Router, F

from .dishes import dishes_router
from .start import start_router
from .myinfo import myinfo_router
from .review_dialog import review_router
from .random_recipe import recipe_router
from .house_kg import house_router
from .group import group_router


private_router = Router()
private_router.include_routers(dishes_router, start_router,
                               myinfo_router, recipe_router, house_router,
                               review_router)

private_router.message.filter(F.chat.type == 'private')
