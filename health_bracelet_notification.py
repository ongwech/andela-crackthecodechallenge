#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'activityAlerts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY distances
#  2. INTEGER d
#

def activityAlerts(distances, d):
    # Write your code here
    notification = 0

    dist = distances[:d]

    def findIdx(st, ed, v):
        if (dist[st] == v):
            return st
        if (dist[ed] == v):
            return ed
        if st == ed or st + 1 == ed:
            return ed

        if dist[int((st + ed) / 2)] <= v:
            return findIdx(int((st + ed) / 2), ed, v)
        else:
            return findIdx(st, int((st + ed) / 2), v)

    dist.sort()
    for i in range(d, n):
        if d % 2 == 1:
            m = dist[int(d / 2)] * 2
        else:
            m = dist[int(d / 2)] + dist[int(d / 2) - 1]
        if distances[i] >= m:
            notification += 1
        del dist[findIdx(0, d - 1, distances[i - d])]
        dist.insert(findIdx(0, d - 2, distances[i]) + 1, distances[i])

    return (notification)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    distances = list(map(int, input().rstrip().split()))

    result = activityAlerts(distances, d)

    fptr.write(str(result) + '\n')

    fptr.close()