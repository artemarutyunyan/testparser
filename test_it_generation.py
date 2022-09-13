def btc_buy(*vargs):
    btc_cost = int(input('Enter the cost of BTC for today: '))
    investments = int(input('Enter the amount of money you would like to invest: '))
    return print(f'You can buy {(investments/btc_cost):.7f} BTCs')
