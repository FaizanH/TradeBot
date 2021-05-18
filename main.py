import testModules
from time import sleep
from time import gmtime, strftime
import threading

prices = {}  # Historical Data
initialCapital = 0  # Test Cash


def main_thread():
    print("Hello, friend.")


# Driver
if __name__ == '__main__':
    print('--- Welcome to The Stonks Markets ---')


def scheduler():
    # Store price at 10s
    while True:
        testModules.store_price(strftime('%Y-%m-%d %H:%M:%S', gmtime()), prices)
        print(prices)
        sleep(10)


b = threading.Thread(name='scheduler', target=scheduler)
f = threading.Thread(name='foreground', target=main_thread)

b.start()
f.start()
