#!/bin/python3

import math
import os
import random
import re
import sys

def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if (i % 3 == 0) and (i % 6 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 6 == 0:
            print("Buzz")
        else:
            print(n)

if __name__ == '__main__':
    n = 15 #int(input().strip())

    fizzBuzz(n)
