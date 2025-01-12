from aiogram import Dispatcher, types
from sqlalchemy.future import select
from bot.models import async_session, Category, Product
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_categories(message: types.Message):
    """Show categories to the user."""
    async with async_session() as session:
        result = await session.execute(select(Category))
        categories = result.scalars().all()

        if not categories:
            await message.answer("Каталог пуст.")
            return

        buttons = [InlineKeyboardButton(text=cat.name, callback_data=f"category_{cat.id}") for cat in categories]
        keyboard = InlineKeyboardMarkup(row_width=2).add(*buttons)
        await message.answer("Выберите категорию:", reply_markup=keyboard)


async def show_products(callback_query: types.CallbackQuery):
    """Show products in a category."""
    category_id = callback_query.data.split("_")[1]
    async with async_session() as session:
        result = await session.execute(select(Product).where(Product.category_id == category_id))
        products = result.scalars().all()

        if not products:
            await callback_query.message.answer("В этой категории пока нет товаров.")
            return

        for product in products:
            text = f"**{product.name}**\nЦена: {product.price} XMR"
            photo = product.photo or None
            await callback_query.message.answer_photo(photo, caption=text) if photo else \
                await callback_query.message.answer(text)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(show_categories, commands=["catalog"])
    dp.register_callback_query_handler(show_products, lambda c: c.data.startswith("category_"))
