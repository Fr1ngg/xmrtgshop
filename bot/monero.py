import requests
from bot.config import MONERO_RPC_URL, MONERO_WALLET_PASSWORD


def call_rpc(method, params=None):
    """Generic RPC call to Monero."""
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "id": "0",
        "method": method,
        "params": params or {}
    }
    response = requests.post(MONERO_RPC_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("result")


def create_address(label):
    """Create a new subaddress with a label."""
    return call_rpc("create_address", {"account_index": 0, "label": label})["address"]


def get_balance(address):
    """Retrieve the balance for a specific subaddress."""
    result = call_rpc("get_balance", {"account_index": 0})
    for subaddress in result["per_subaddress"]:
        if subaddress["address"] == address:
            return subaddress["balance"] / 1e12  # Convert to XMR
    return 0.0


def get_transfers(address):
    """Retrieve incoming transactions for a subaddress."""
    result = call_rpc("get_transfers", {"account_index": 0})
    return [tx for tx in result.get("in", []) if tx["address"] == address]
