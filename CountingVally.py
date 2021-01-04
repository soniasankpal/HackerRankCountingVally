#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley=0
    height=0
    for i in range(0,len(path)):
        if(path[i]=='U'):
            height=height+1
        else:
            height=height-1
        if(height==0 and path[i]=='U'):
            valley=valley+1
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(raw_input().strip())

    path = raw_input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
 
