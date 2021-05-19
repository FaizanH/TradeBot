from testModules import should_buy, should_sell, test_buy, test_sell
from time import sleep
from time import gmtime, strftime
import threading


def main_t():
    pass


# Driver
if __name__ == '__main__':
    print('--- Welcome to TSM ---')


def scheduler_t():
    while True:
        # store_price(strftime('%Y-%m-%d %H:%M:%S', gmtime()))
        print('- Running get_latest_percent_change_1h test')
        if should_buy():
            print('Target % met. Buying...')

        if should_sell():
            print('Trailing stop loss conditions met. Selling...')

        sleep(5)


b = threading.Thread(name='scheduler', target=scheduler_t)
f = threading.Thread(name='foreground', target=main_t)

b.start()
f.start()
