import requests
import json
import redis


def get_latest_eth():
    cs_prices = requests.get("https://www.coinspot.com.au/pubapi/latest/ETH").json()['prices']
    return cs_prices['ask']


def get_latest_prices():
    response = requests.get("https://www.coinspot.com.au/pubapi/latest")
    return response.text


# Generate historical data
def store_price(currtime, storage):
    storage.__setitem__(currtime, get_latest_eth())


# Devise MACD Strategy
