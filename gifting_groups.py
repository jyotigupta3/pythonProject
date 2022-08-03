#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    # Write your code here
    count = 0
    length = len(related)
    related = convertToArray(related)

    for indx in range(length):
        if related[indx][indx] == 1:
            count += 1
            dfs(indx, length, related)
    return count


def dfs(idx, length, matrix):
    if matrix[idx][idx] == 0:
        return
    for i in range(length):
        if matrix[idx][i] == 1:
            matrix[idx][i] = 0
            dfs(i, length, matrix)


def convertToArray(s):
    result = []
    for char in s:
        result.append([int(x) for x in char])
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    related_count = int(input().strip())

    related = []

    for _ in range(related_count):
        related_item = input()
        related.append(related_item)

    result = countGroups(related)

    # fptr.write(str(result) + '\n')
    print(str(result) + '\n')
    # fptr.close()
