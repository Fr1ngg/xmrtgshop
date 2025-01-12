import os

# Конфигурация бота
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Telegram Bot API токен

# Monero RPC
MONERO_RPC_URL = os.getenv("MONERO_RPC_URL", "http://remote-node:18089/json_rpc")
MONERO_WALLET_PASSWORD = os.getenv("MONERO_WALLET_PASSWORD", "your_wallet_password")

# База данных
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///database.db")
