import testModules
from time import sleep
from time import gmtime, strftime

prices = {}  # Historical Data
initialCapital = 0  # Test Cash

# Driver
if __name__ == '__main__':
    # Store price at 10s
    while True:
        testModules.store_price(strftime("%Y-%m-%d %H:%M:%S", gmtime()), prices)
        sleep(10)
