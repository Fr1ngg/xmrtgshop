
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from bot.config import DATABASE_URL

Base = declarative_base()

# Настройка базы данных
engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class User(Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    telegram_id = sqlalchemy.Column(sqlalchemy.BigInteger, unique=True, nullable=False)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    monero_address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    balance = sqlalchemy.Column(sqlalchemy.Float, default=0.0)
