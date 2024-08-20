#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product



#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


    
def hourglassSum(arr):
    center_cp = list(product(range(1, 5), repeat=2))
    rel_x, rel_y = [-1, 0, 1], [-1, 1]
    rel_cp = list(product(rel_x, rel_y))
    
    sums = []
    for x, y in center_cp:
        summ = arr[y][x]
        for i, j in rel_cp:
            summ += arr[y+j][x+i]
        sums.append(summ)
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
