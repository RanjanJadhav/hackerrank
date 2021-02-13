#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(n,arr):
    # diagonal = 0
    # anti_diagonal = 0
    # for i in range(n):
    #     diagonal = diagonal + arr[i][i]
    #     anti_diagonal = anti_diagonal + arr[i][n-i-1]
    # return abs(diagonal - anti_diagonal)

    total = 0
    for i in range(n):
        total = total + arr[i][i] - arr[i][n-i-1] 
    return abs(total)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n,arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
