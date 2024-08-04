from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .settings import settings
from bot.src.handlers import router

TOKEN = settings.BOT_TOKEN

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    dp.include_router(router)
    await dp.start_polling(bot)
