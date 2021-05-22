from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import config
import requests
import json

# _api_key = config._api_key
# cmc = CoinMarketCapAPI(_api_key)

prices = {}  # Historical Data
percentages_history_1h = []
capital = 0  # Test Cash
netProfitLoss = 0  # Positive = profit, Negative = loss


def percent_change_custom(pinitial, pcurrent):
    p = ((float(pcurrent) - float(pinitial))/float(pinitial)) * 100
    return str(p)


# def get_latest_percent_1h():
#     try:
#         cmc_data = cmc.cryptocurrency_listings_latest().data
#         for x in cmc_data:
#             if x['symbol'] == 'ADA':
#                 p = json.loads(json.dumps(x))['quote']['USD']['percent_change_1h']
#                 return p
#     except ValueError:
#         print('JSON decoding has failed')


# Devise MACD Strategy

# 5% increase in 2.5 min
# obvious - 2.5 2.5 2.5

# 15% increase in
# big negative value in large window
# small positive in small window
# buying the dip
def should_buy_sell_wait(p, interval):
    # Check 1m, 2.5m, 5m, 7.5m, 10m, 15m, 30, 1h, 3h
    # if 10 interval > 10% and 60 interval positive and 180 interval positive

    # Notify speed fast increase

    # Notify speed slow increase - Uptrend

    # Trailing stop loss notification
    # Set buy_price = peak
    # Latest peak compared to current price
    # If current price < latest peak * 95%
    # Price has dropped 5%, sell

    if 15 > float(p) > 5:
        print("Percentage INCREASE 5-15% over " + str(interval) + "min")
        return 'buy'
    elif float(p) > 15:
        print("Percentage INCREASE over 15% over " + str(interval) + "min")
        return 'buy'
    elif float(p) <= -10:
        print("Percentage DROP >= -10% over " + str(interval) + "min")
        return 'sell'
    return ''


# Simulation environment with account balance, crypto balance

# Messenger notification api


# Getters and Setters
def get_current_profits():
    pass


def get_percentages_1h():
    return percentages_history_1h


def get_prices():
    return prices


# Test Modules
def test_buy(capital, netpl):
    pass


def test_sell():
    pass


# Prices

def get_latest_eth():
    cs_prices = requests.get('https://www.coinspot.com.au/pubapi/latest/ETH').json()['prices']
    return cs_prices['ask']


def get_latest_prices():
    response = requests.get('https://www.coinspot.com.au/pubapi/latest')
    return response.text


def store_price(currtime):
    prices.__setitem__(currtime, get_prices())


def average_prices_hourly():
    prices_hour_past = [key for key in prices if '2021-05-18 10:' in key.lower()]  # Filter timestamp keys
    hourly_sum = 0
    for key in prices_hour_past:
        hourly_sum += float(prices[key])
    return hourly_sum / len(prices_hour_past)
