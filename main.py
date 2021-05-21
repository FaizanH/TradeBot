from testModules import percent_change_custom, get_latest_eth, should_buy_sell_wait, test_buy, test_sell
from time import sleep
from time import gmtime, strftime
import threading


print('Price initialisation successful')


def main_t():
    pass


# Driver
if __name__ == '__main__':
    print('--- Welcome to TSM ---\n')


def scheduler_t():
    interval = 0
    p = 0
    prices = []
    startpr = float(get_latest_eth())

    sleep(5)

    print('- RUNNING 2.5/15 TESTS\n')
    print('TIME | $PRICE | % Δ 10MIN')
    while True:
        # Append to file instead or using sliding window approach
        prices.append(float(get_latest_eth()))
        p = percent_change_custom(startpr, prices[-1])
        if interval == 0:
            print(str(interval) + ' | ' + str("{:.8}".format(prices[-1])) + ' | ' + str(0))
        else:
            print(str(interval) + ' | ' + str("{:.8}".format(prices[-1])) + ' | ' + str("{:.4}".format(p)))

        if interval >= 10:  # Set trail start
            startpr = prices[-4]
        if interval % 10 == 0 and interval != 0:
            print('TRAIL PRICE SET: LAST 10MIN')

        outcome = should_buy_sell_wait(p, interval)
        if outcome == 'buy' and interval > 2.5:
            print('Buying...')
        elif outcome == 'sell':
            print('Selling...')
        elif outcome == 'wait':
            print('Waiting...')

        interval += 2.5
        sleep(5)  # Check at 2.5 minute intervals

# store_price(strftime('%Y-%m-%d %H:%M:%S', gmtime()))


b = threading.Thread(name='scheduler', target=scheduler_t)
f = threading.Thread(name='foreground', target=main_t)

b.start()
f.start()
