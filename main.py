from testModules import get_latest_pchange_custom, get_latest_eth, should_buy, should_sell, test_buy, test_sell
from time import sleep
from time import gmtime, strftime
import threading


print('Price initialisation successful')

def main_t():
    pass


# Driver
if __name__ == '__main__':
    print('--- Welcome to TSM ---')


def scheduler_t():
    prices = []
    initialprice = float(get_latest_eth())  # Needs to have atleast 2 elements to comapare
    intervalcount = 0
    pchange = 0
    print('- Running 2.5/15 minute tests')
    while True:
        # For every 2.5 mins
        # Save initial price
        # After 15 min replace initial price with current price
        # or
        # Save price in list
        # After 15 mins set trailing price

        prices.append(float(get_latest_eth()))
        pchange = get_latest_pchange_custom(initialprice, prices[-1])

        print(str(intervalcount)+' min' '- $' + str(prices[-1]) + '| % Change = ' + str(pchange))
        if intervalcount % 15 == 0 and intervalcount != 0:
            print('15 min mark - new reset')
            initialprice = prices[-1]

        # print('- Running get_latest_percent_change_1h test')
        if should_buy(pchange, intervalcount) and intervalcount > 2.5:
            print('Target % met. Buying...')

        if should_sell():
            print('Trailing stop loss conditions met. Selling...')

        intervalcount += 2.5
        sleep(5)  # Check at 2.5 minute intervals

       # store_price(strftime('%Y-%m-%d %H:%M:%S', gmtime()))


b = threading.Thread(name='scheduler', target=scheduler_t)
f = threading.Thread(name='foreground', target=main_t)

b.start()
f.start()
