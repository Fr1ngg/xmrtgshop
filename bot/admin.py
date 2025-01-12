from aiogram import Dispatcher, types
from sqlalchemy.future import select
from bot.models import async_session, Category
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ADMIN_IDS = [123456789]  # ID администраторов


async def admin_menu(message: types.Message):
    """Show admin menu."""
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("У вас нет прав доступа.")
        return

    buttons = [
        InlineKeyboardButton(text="Управление категориями", callback_data="admin_categories"),
        InlineKeyboardButton(text="Управление товарами", callback_data="admin_products")
    ]
    keyboard = InlineKeyboardMarkup(row_width=1).add(*buttons)
    await message.answer("Админ-меню:", reply_markup=keyboard)


async def manage_categories(callback_query: types.CallbackQuery):
    """Manage categories."""
    async with async_session() as session:
        result = await session.execute(select(Category))
        categories = result.scalars().all()

        buttons = [InlineKeyboardButton(text=f"Удалить: {cat.name}", callback_data=f"delete_cat_{cat.id}")
                   for cat in categories]
        buttons.append(InlineKeyboardButton(text="Добавить категорию", callback_data="add_category"))
        keyboard = InlineKeyboardMarkup(row_width=1).add(*buttons)
        await callback_query.message.answer("Управление категориями:", reply_markup=keyboard)


async def add_category(callback_query: types.CallbackQuery):
    """Add a new category."""
    await callback_query.message.answer("Введите название новой категории:")

    @dp.message_handler()
    async def save_category(message: types.Message):
        async with async_session() as session:
            new_category = Category(name=message.text)
            session.add(new_category)
            await session.commit()
            await message.answer(f"Категория '{message.text}' добавлена.")
        dp.message_handlers.unregister(save_category)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_menu, commands=["admin"])
    dp.register_callback_query_handler(manage_categories, lambda c: c.data == "admin_categories")
    dp.register_callback_query_handler(add_category, lambda c: c.data == "add_category")
