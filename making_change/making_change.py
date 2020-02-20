#!/usr/bin/python

import sys
from functools import lru_cache

# Currency
# nickel = 5 cents
# dime = 10 cents
# quarter = 25 cents
# half-dollar = 50 cents

# calculate the number of ways change can be calculated from the given denominations

@lru_cache(maxsize = 2000)
def making_change(amount, denominations):
  denominations_tuple = tuple(denominations)
  if type(amount) != int:
    raise TypeError('amount must be an integer')
  if amount < 0:
    return 0
  elif 0 < amount < 5:
    return 1
  else:
    return sum([making_change(amount - d, denominations_tuple) for d in denominations_tuple])


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
