#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getHeaviestPackage' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY packageWeights as parameter.
#

def getHeaviestPackage(packageWeights):
    # Write your code here
    length = 0
    # length = len(packageWeights)-1
    while length < len(packageWeights):
        print("length: ", length)
        p1, p2 = packageWeights[length], packageWeights[length + 1]
        print("p1: ", p1)
        print("p1: ", p2)
        if p1 < p2:
            packageWeights[length + 1] = p1 + p2
            print("packageWeights[length+1]: ", packageWeights[length + 1])
            del packageWeights[length]
        length = length + 1
    return max(packageWeights)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    packageWeights_count = int(input().strip())

    packageWeights = []

    for _ in range(packageWeights_count):
        packageWeights_item = int(input().strip())
        packageWeights.append(packageWeights_item)

    result = getHeaviestPackage(packageWeights)
    print(str(result) + '\n')
    # fptr.write(str(result) + '\n')

    # fptr.close()
