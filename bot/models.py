from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import sqlalchemy as sa
from bot.config import DATABASE_URL

Base = declarative_base()

# Database engine and session
engine = create_async_engine(DATABASE_URL, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    telegram_id = sa.Column(sa.BigInteger, unique=True, nullable=False)
    username = sa.Column(sa.String, nullable=True)
    monero_address = sa.Column(sa.String, nullable=False)
    balance = sa.Column(sa.Float, default=0.0)


class Category(Base):
    __tablename__ = "categories"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    products = relationship("Product", back_populates="category", cascade="all, delete")


class Product(Base):
    __tablename__ = "products"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    photo = sa.Column(sa.String, nullable=True)  # URL фото товара
    category_id = sa.Column(sa.Integer, sa.ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")
