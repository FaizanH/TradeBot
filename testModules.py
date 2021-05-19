from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import config
import requests
import json

_api_key = config._api_key

cmc = CoinMarketCapAPI(_api_key)

prices = {}  # Historical Data
percentages_history_1h = []
capital = 0  # Test Cash
netProfitLoss = 0  # Positive = profit, Negative = loss


def get_latest_pchange_1h():
    try:
        cmc_data = cmc.cryptocurrency_listings_latest().data
        for x in cmc_data:
             if (x['symbol'] == 'ADA'):
                 p = json.loads(json.dumps(x))['quote']['USD']['percent_change_1h']
                 return p
    except ValueError:
        print('JSON decoding has failed')

# Devise MACD Strategy
def should_buy():
    # Buy if percentage increase > 5
    if get_latest_pchange_1h() > 5:
        print("Percentage increased by 5% in last hour")
        return True
    return False

def should_sell():
    if get_latest_pchange_1h() < -10:
        print("Percentage just dropped below -10% in last hour")
        return True
    return False

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
    return cs_prices['last']

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
