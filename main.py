import requests


def get_prices():
    response = requests.get("https://www.coinspot.com.au/pubapi/latest")
    return response.text


if __name__ == '__main__':
    print(get_prices())
