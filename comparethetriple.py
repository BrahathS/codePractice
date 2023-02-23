import math
import os
import random
import re
import sys

# Complete the 'compareTriplets' function below.

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

# Input Format
# The first line contains an integer T denoting the number of test cases.

# The first line of each test case contains 3 space-separated integers a0, a1, and a2,
# describing the respective values in triplet a.

# The second line of each test case contains 3 space-separated integers b0, b1, and b2,
# describing the respective values in triplet b.


def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            continue
    return [alice, bob]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
