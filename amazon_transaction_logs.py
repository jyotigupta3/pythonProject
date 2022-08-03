#!/bin/python3

import math
import os
import random
import re
import sys
import collections


#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

def processLogs(logs, threshold):
    # Write your code here
    res = []
    dict = collections.defaultdict(int)
    for each_rows in logs:
        row = ''.join(each_rows)
        temp = row.split()
        if temp[0] != temp[1]:
            dict[temp[1]] += 1
        dict[temp[0]] += 1

    for key, val in dict.items():
        if val >= threshold:
            res.append(key)
    res.sort()
    return res


"""
4
1 2 50
1 7 70
1 3 20
2 2 17
2
"""
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())
    result = processLogs(logs, threshold)
    print('\n'.join(result))
    print("\n")

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
