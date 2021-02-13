#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles_count, candles):
    # Write your code here
    # count = 0
    # tallest_candle = max(candles)
    # for _ in candles:
    #     if _ == tallest_candle:
    #         count = count + 1

    # print(count)

    count = 0
    max_age = 0
    for i in range(candles_count):
        if candles[i] > max_age:
            max_age = candles[i] 
            count = 0
        if candles[i] == max_age:
            count = count + 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles_count, candles)

    # fptr.write(str(result) + '\n')

    # fptr.close()
