#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridCheck(grid):
    n = len(grid)
    k = len(grid[0])
    for i in range(n):
        for j in range(k-1):
            if(grid[i][j]>grid[i][j+1]):
                return False
            
    for i in range(k):
        for j in range(n-1):
            if(grid[j][i]>grid[j+1][i]):
                return False
    return True


def gridChallenge(grid):
    if(gridCheck(grid)):
        return "YES"
    sorted_arr = []
    for i in range(len(grid)):
        sorted_arr.append(sorted(grid[i]))
    if(gridCheck(sorted_arr)):
        return "YES"
    else:
        return "NO"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
