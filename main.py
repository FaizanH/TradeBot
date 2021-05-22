from testModules import percent_change_custom, get_latest_eth, should_buy_sell_wait, send_notify
from time import sleep
import threading


print('Price initialisation successful')


def main_t():
    pass


# Driver
if __name__ == '__main__':
    print('--- Welcome to TSM ---\n')
    send_notify("test msg")


def scheduler_t():
    interval = 0
    p = 0
    prices = []
    per_2_5 = 0
    per_10 = 0
    per_30 = 0

    sleep(5)

    print('- RUNNING 2.5/15 TESTS\n')
    print('- DO NOT USE DATA FROM FIRST INTERVAL\n')
    print('TIME | $PRICE | % Δ 2.5MIN | % Δ 10MIN | % Δ 30MIN')
    while True:
        # Append to file instead or using sliding window approach
        prices.append(get_latest_eth())

        if interval >= 2.5:
            start_price_2_5 = prices[-2]
            per_2_5 = percent_change_custom(start_price_2_5, prices[-1])
        if interval >= 10:
            start_price_10 = prices[-4]
            per_10 = percent_change_custom(start_price_10, prices[-1])
        if interval >= 30:
            start_price_30 = prices[-12]
            per_30 = percent_change_custom(start_price_30, prices[-1])

        print(str(interval) + ' | ' + prices[-1] + ' | ' + str(per_2_5) + ' | ' + str(per_10) + ' | ' + str(per_30))
        # last 4 = 10MIN, last 12 = 30MIN

        if interval % 2.5 == 0 and interval != 0:
            pass
        elif interval % 10 == 0 and interval != 0:
            print('10MIN TRAIL SET')
        elif interval % 30 == 0 and interval != 0:
            print('30MIN TRAIL SET')

        # outcome = should_buy_sell_wait(p, interval)
        #
        # if outcome == 'buy' and interval > 2.5:
        #     print('Buying...')
        # elif outcome == 'sell':
        #     print('Selling...')
        # elif outcome == 'wait':
        #     print('Waiting...')

        interval += 2.5
        sleep(5)  # Check at 2.5 minute intervals

# store_price(strftime('%Y-%m-%d %H:%M:%S', gmtime()))


b = threading.Thread(name='scheduler', target=scheduler_t)
f = threading.Thread(name='foreground', target=main_t)

# b.start()
f.start()
