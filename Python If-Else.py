#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        for i in range(2,6):
            if i == n:
                print("Not Weird")
        for i in range(6,21):
            if i == n:
                print("Weird")
        if n > 20:
            print("Not Weird")
    if n % 2 != 0:
        print("Weird")
