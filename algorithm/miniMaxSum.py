#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    tot_max = 0
    tot_min = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            tot_max = tot_max + arr[i]
            tot_min = tot_min + arr[i+1]
        else:
            tot_max = tot_max + arr[i+1]
            tot_min = tot_min +arr[i]

    print(f'{tot_min} {tot_max}')


    # tot_max = arr[0]
    # tot_min = arr[0]
    # total = 0
    # for i in range(len(arr)):
    #     total = total + arr[i]
    #     if arr[i] > tot_max:
    #         tot_max = arr[i]
    #     else:
    #         tot_min = arr[i]
    # print(f'{total - tot_max} {total - tot_min} ')

    # print(f'{sum(arr)-max(arr)} {sum(arr)-min(arr)}')



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
