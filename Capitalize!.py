#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in range (0,len(s)):
        if i==0:
            s =  s[i].upper() + s[i+1:]
        elif s[i]==" ":
            s =  s[:i+1] + s[i+1].upper() + s[i+2:]
            
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
