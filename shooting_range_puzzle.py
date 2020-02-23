#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isWin' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING setup
#

def isWin(n, setup):
    # return WIN if you win otherwise return LOSE
    win = [0]
    for n in range(1, 301):
        s = set()
        for a in range(n // 2 + 1):
            s.add(win[a] ^ win[n - 1 - a])
            s.add(win[a] ^ win[n - 2 - a])
        m = 0
        while m in s:
            m += 1
        win.append(m)

    def solve(setup_x):
        r = 0
        for s in setup_x.split('X'):
            r ^= win[len(s)]

        return "WIN" if r else "LOSE"

    for _ in range(n):
        return (solve(setup))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        setup = input()

        result = isWin(n, setup)

        fptr.write(result + '\n')

    fptr.close()