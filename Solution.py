#!/bin/python3

import os
import sys

#
# Complete the movingTiles function below.
#
from math import sqrt
def movingTiles(l, s1, s2, queries):
    ans = []
    for area in queries:
        if area <= l*l:
            lq = sqrt(area)
            dq = sqrt(lq * lq * 2)
            dl = sqrt(l * l * 2)
            relative_distance = dl - dq
            t = relative_distance / abs(s2 - s1)
            ans.append(t)
    return ans
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
