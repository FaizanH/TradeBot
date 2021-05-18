from coinspot import CoinSpot
import config
import requests

_api_key = config._api_key
_api_secret = config._api_secret

coin = CoinSpot(_api_key, _api_secret)
prices = {}  # Historical Data
capital = 0  # Test Cash
netProfitLoss = 0  # Positive = profit, Negative = loss


def get_latest_eth():
    cs_prices = requests.get('https://www.coinspot.com.au/pubapi/latest/ETH').json()['prices']
    return cs_prices['last']


def get_latest_custom():
    try:
        print(coin.my_balances())
    except ValueError:
        print('JSON decoding has failed')


def get_latest_prices():
    response = requests.get('https://www.coinspot.com.au/pubapi/latest')
    return response.text


# Generate historical data
def store_price(currtime):
    prices.__setitem__(currtime, get_latest_eth())


def average_prices_hourly():
    prices_hour_past = [key for key in prices if '2021-05-18 10:' in key.lower()]  # Filter timestamp keys
    hourly_sum = 0
    for key in prices_hour_past:
        hourly_sum += float(prices[key])
    return hourly_sum / len(prices_hour_past)


# Devise MACD Strategy
def should_buy():
    pass


def should_sell():
    pass


# Getters and Setters
def get_current_profits():
    pass


def get_prices():
    return prices


# Test Modules
def test_buy(capital, netpl):
    pass


def test_sell():
    pass
