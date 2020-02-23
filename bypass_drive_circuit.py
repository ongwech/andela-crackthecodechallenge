#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bypassCircuit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY stations as parameter.
#

def bypassCircuit(stations):
    # Write your code here
    # print(stations)
    l = len(stations)

    s, c = 0, 0

    for i in range(l):
        station = stations[i]
        p = station[0]
        d = station[1]
        if c + p < d:
            s = i + 1
            c = 0
        else:
            c += p - d

    return (s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    stations = []

    for _ in range(n):
        stations.append(list(map(int, input().rstrip().split())))

    result = bypassCircuit(stations)

    fptr.write(str(result) + '\n')

    fptr.close()