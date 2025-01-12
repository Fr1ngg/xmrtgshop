import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Получаем токен из переменной окружения
API_TOKEN = os.getenv('API_TOKEN')

# Проверка, если токен не найден
if not API_TOKEN:
    raise ValueError("API_TOKEN не найден! Проверьте переменную окружения или .env файл.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Включаем логирование middleware
dp.middleware.setup(LoggingMiddleware())

# Команда /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой бот.")

# Команда /help
@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer("Список доступных команд: /start, /help")

# Обработчик сообщений
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
