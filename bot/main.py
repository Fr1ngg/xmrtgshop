from aiogram import Bot, Dispatcher, executor
from bot.config import BOT_TOKEN
from bot.handlers import register_user_handlers
from bot.admin import register_admin_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Register handlers
register_user_handlers(dp)
register_admin_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
