#!/usr/bin/env python

import sys

# We have to set a higher max recursion depth

sys.setrecursionlimit(100000)

# Functions hand translated from C
# https://www.youtube.com/watch?v=i7sm9dzFtEI

def ackermann(m, n):
    if m == 0:
        ans = n + 1
    elif n == 0:
        ans = ackermann(m - 1, 1)
    else:
        ans = ackermann(m - 1, ackermann(m, n - 1))
    return ans

def loop():
    for i in range(6):
        for j in range(6):
            print("Ackermann of (", i, ", ", j, ") is: ", ackermann(i, j), sep="")

loop()
