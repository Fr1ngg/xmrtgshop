import os

# Telegram Bot API Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Monero RPC Settings
MONERO_RPC_URL = os.getenv("MONERO_RPC_URL", "http://127.0.0.1:18082/json_rpc")
MONERO_RPC_LOGIN = os.getenv("MONERO_RPC_LOGIN", "user:password")  # Логин и пароль RPC
MONERO_WALLET_PASSWORD = os.getenv("MONERO_WALLET_PASSWORD", "your_wallet_password")  # Пароль кошелька

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///database.db")
