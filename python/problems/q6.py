#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#


def truckTour(petrolpumps):
    total_petrol = 0
    total_distance = 0
    balance = 0
    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        total_petrol += petrol
        total_distance += distance
        balance = total_petrol - total_distance
        starting_point = 0
        
        if balance < 0:
            starting_point = i+1
            balance = 0
            
    if total_petrol >= total_distance:
        return starting_point
    else:
        return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
