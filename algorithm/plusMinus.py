#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(n,arr):
    positives = 0
    negatives = 0
    zeros = 0
    for ech_digit in arr:
        if ech_digit>0:
            positives= positives +1
        elif ech_digit<0:
            negatives=negatives+1
        else:
            zeros = zeros +1
    print(positives/n)
    print(negatives/n)
    print(zeros/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n,arr)


# >>> 125650429603636838/(2**53)
# 13.949999999999999

# >>> 234042163/(2**24)
# 13.949999988079071

# >>> a = 13.946
# >>> print(a)
# 13.946
# >>> print("%.2f" % a)
# 13.95
# >>> round(a,2)
# 13.949999999999999
# >>> print("%.2f" % round(a, 2))
# 13.95
# >>> print("{:.2f}".format(a))
# 13.95
# >>> print("{:.2f}".format(round(a, 2)))
# 13.95
# >>> print("{:.15f}".format(round(a, 2)))
# 13.949999999999999