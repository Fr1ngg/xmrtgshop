from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import logging

API_TOKEN = '8069011753:AAFhydbTVyUUCij4sEbVtOZZl2zttQE1tew'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(Command("start"))
async def cmd_start(message):
    await message.answer("Hello! I'm your bot.")

# Заменяем executor.start_polling() на dp.run_polling()
if __name__ == '__main__':
    dp.run_polling()
