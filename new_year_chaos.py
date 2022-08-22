#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    length = len(q)
    bribe = 0
    chaotic = ""
    for i in range(length):
        if q[i]>i+3:
            chaotic += "Too chaotic"
            break
        for j in range(max(0, q[i]-2), i):
            if q[i]<q[j]:
                bribe += 1
    if chaotic:
        print(chaotic)
        # print("Too chaotic")
    else:
        print(bribe)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
