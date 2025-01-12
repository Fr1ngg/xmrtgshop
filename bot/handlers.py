from aiogram import Dispatcher, types
from bot.monero import create_address, get_balance, get_transfers
from bot.models import User, async_session
from sqlalchemy.future import select

async def start_command(message: types.Message):
    async with async_session() as session:
        user = await session.execute(select(User).where(User.telegram_id == message.from_user.id))
        user = user.scalar_one_or_none()

        if not user:
            address = create_address(str(message.from_user.id))
            new_user = User(
                telegram_id=message.from_user.id,
                username=message.from_user.username or "Unknown",
                monero_address=address,
            )
            session.add(new_user)
            await session.commit()
            await message.answer(f"Добро пожаловать! Ваш Monero-адрес: {address}")
        else:
            await message.answer("Вы уже зарегистрированы!")

async def balance_command(message: types.Message):
    async with async_session() as session:
        user = await session.execute(select(User).where(User.telegram_id == message.from_user.id))
        user = user.scalar_one_or_none()
        if user:
            balance = get_balance(user.monero_address)
            await message.answer(f"Ваш баланс: {balance:.12f} XMR")
        else:
            await message.answer("Вы не зарегистрированы!")
