#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Initialise variables to track the current minimum price, the index of the current minimum to ensure it's lower than the potential maximum, and the profit.
    min_price = prices[0]
    min_price_index = 0
    # Initialised as the first potential profit.
    profit = prices[1] - prices[0]

    # Loop through prices, checking against the potential profit and minimum price.
    for p in prices:
        # Check if the current price is lower than the minimum price - if so, set to minimum.
        if p < min_price:
            min_price = p
            min_price_index = prices.index(p)
        # Check if the profit with the current value is larger than the existing profit, and whether it's index is larger the current minimum index.
        if p - min_price > profit and prices.index(p) > min_price_index:
            profit = p - min_price

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
