from testModules import percent_change_custom, get_latest_eth, get_latest_ada, should_buy_sell_wait, send_notify
from time import sleep, gmtime, strftime
from datetime import datetime
from pytz import timezone

print('Price initialisation successful')
tz = timezone('Australia/Sydney')
datetime.now(tz)

# Driver
if __name__ == '__main__':
    print('--- Welcome to TSM ---\n')
    prices = []
    prices_ada = []
    interval = 0
    pi_1, pi_3, pi_5, pi_7, pi_10, pi_15, pi_30, pi_60, pi_180 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    ps_1, ps_3, ps_5, ps_7, ps_10, ps_15, ps_30, ps_60, ps_180 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    sleep(5)

    time = "SCRIPT STARTED - " + str(datetime.now(tz))
    print(time)
    print('- DO NOT USE DATA FROM FIRST INTERVAL\n')
    print('TIME | $ETH | $ADA | % Δ/MIN | % Δ/3MIN | % Δ/5MIN | % Δ/10MIN | % Δ/30MIN')
    send_notify(time)
    while True:
        # Append to file instead
        prices.append(get_latest_eth())
        prices_ada.append(get_latest_ada())

        if interval >= 1:
            ps_1 = prices[-2]
            pi_1 = percent_change_custom(ps_1, prices[-1])
        if interval >= 3:
            ps_3 = prices[-3]
            pi_3 = percent_change_custom(ps_3, prices[-1])
        if interval >= 5:
            ps_5 = prices[-3]
            pi_5 = percent_change_custom(ps_5, prices[-1])
        if interval >= 10:
            ps_10 = prices[-10]
            pi_10 = percent_change_custom(ps_10, prices[-1])
        if interval >= 30:
            ps_30 = prices[-30]
            pi_30 = percent_change_custom(ps_30, prices[-1])

        line = str(interval) + 'MINS | ' + prices[-1] + ' | ' + prices_ada[-1] + ' | ' + str(pi_1) + ' | ' + str(pi_3)\
            + ' | ' + str(pi_5) + ' | ' + str(pi_10) + ' | ' + str(pi_30)
        print(line)  # last 4 = 10MIN, last 12 = 30MIN

        analysis = should_buy_sell_wait(pi_1, pi_3, pi_5, pi_7, pi_10, pi_15, pi_30, pi_60, pi_180, interval)
        if interval > 10 and analysis != '':
            send_notify(analysis + line)
            print(analysis)

        interval += 1

        if interval == 3600 or interval == 7200 or interval == 10800 or interval == 14400 or interval == 18000:
            file = open("logs/Exchange_Price_log.txt", "w")
            for x in prices:
                file.write(strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' - ' + x + '\n')
            file.close()
        sleep(60)  # Check at 1 minute intervals
