from aiogram import Bot, Dispatcher, executor
from bot.config import BOT_TOKEN
from bot.handlers import start_command, balance_command

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(start_command, commands=["start"])
dp.register_message_handler(balance_command, commands=["balance"])

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
