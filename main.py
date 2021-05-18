from testModules import get_prices, store_price, test_buy, test_sell, average_prices_hourly, get_latest_custom
from time import sleep
from time import gmtime, strftime
import threading


def main_t():
    get_latest_custom()


# Driver
if __name__ == '__main__':
    print('--- Welcome to TSM ---')


def scheduler_t():
    # Store price and averages
    while True:
        # Generate historical data
        store_price(strftime('%Y-%m-%d %H:%M:%S', gmtime()))
        # Generate Hourly Averages
        if bool(get_prices() is False):
            print("Dict empty!")
        # else:
            # print("Average price (Past Hour): " + str(average_prices_hourly()))

        sleep(10)


b = threading.Thread(name='scheduler', target=scheduler_t)
f = threading.Thread(name='foreground', target=main_t)

b.start()
f.start()
