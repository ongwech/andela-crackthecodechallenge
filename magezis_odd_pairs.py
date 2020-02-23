#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def countPairs(a):
    # Write your code here
    d = {}
    for j in a: d[j] = d.get(j, 0) + 1
    ret = sum(d[i] * (d[i] - 1) for i in d)
    return (ret)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = countPairs(a)

        fptr.write(str(result) + '\n')

    fptr.close()