import os

# Telegram Bot API Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Monero RPC Settings
MONERO_RPC_URL = os.getenv("MONERO_RPC_URL", "http://remote-node:18089/json_rpc")
MONERO_WALLET_PASSWORD = os.getenv("MONERO_WALLET_PASSWORD", "your_wallet_password")

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///database.db")
