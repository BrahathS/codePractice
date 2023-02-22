# special subarray

# you are given an array a of length N. a subarray is special if the  XOR and sum of the subarray are the same. find the number of elements special subarray of A.

# Input Format

# The first line contains an integer T, the number of test cases. Each test case consists of two lines. The first line contains an integer N, the length of the array A. The second line contains N space-separated integers, denoting the array A.

# Constraints

# 1 <= T <= 10
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^5

# Output Format

# For each test case, print the number of special subarrays of A.

# Sample Input 0

# 2
# 3
# 1 2 3
# 4

# 1 2 3 4

# Sample Output 0

# 2
# 4

# Explanation 0

# For the first test case, the special subarrays are [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]. There are 6 such subarrays, but only 2 are distinct.

# Write your code here
import math
import os
import random
import re
import sys


def specialSubarray(ar):
    count = 0
    for i in range(len(ar)):
        for j in range(i, len(ar)):
            if sum(ar[i : j + 1]) == ar[i] ^ ar[j]:
                count += 1
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        a = list(map(int, input().rstrip().split()))
        result = specialSubarray(a)
        fptr.write(str(result) + "")
