# Function Description

# Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

# simpleArraySum has the following parameter(s):

#     ar: an array of integers

# Input Format

# The first line contains an integer,
# , denoting the size of the array.
# The second line contains

# space-separated integers representing the array's elements.

# Constraints

# 0 < n, ar[i] <= 1000

# Output Format

# Print the sum of the array's elements as a single integer.

import math
import os
import random
import re
import sys


def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + "\n")
    fptr.close()
