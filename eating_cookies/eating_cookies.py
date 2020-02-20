#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# Decision tree - because the cookie monster can eat 1, 2 or 3 cookies at a time, in order to calculate the function for n, you need the results of n-1, n-2 and n-3 as there are 3 possible ways for the cookie monster to start - eating 1 cookie, 2 cookies or 3 cookies.
def eating_cookies(n, cache={}):
    # Check that the value is an integer.
    # if type(n) != int:
    #     raise TypeError('n must be an integer')
    # Check that the value is not a negative number.
    if n in cache:
        return cache[n]
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        value = (eating_cookies(n-1) +
                    eating_cookies(n-2) + eating_cookies(n-3))
    cache[n] = value
    return value

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
