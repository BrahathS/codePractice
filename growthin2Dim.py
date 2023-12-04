# Growth in 2 Dimensions

# start with an infinite 2 dimensional grid filled with zeros indexed from (1,1) at the bottom left corner with coordinates increase towards the top and right.
# Given a series of coordinates (r,c) where r is the ending row and c is the ending column, add 1 to each element in the range from (1,1) to (r,c) inclusive.
# once all coordinates are processed determine how many cells contain the maximal value in the grid.

# Example
# upRight = ["1 4", "2 3", "4 1"]

# The two space separated interger within each string repesent r and c respectively.

# function description
# Complete the function countMax in the editor below.
# countMax has the following parameter (s):
#     string upRight[n]: an array of strings where each string is a row of two space separated integers, r and c.
#  return
# long : the number of occurrences of the final grid's maximal element

# Constraints
# 1 <= n <= 100
# 1<= number of rows number of columns <= 10^6

# Input Format for Custom Testing
# The first line contains an integer, n, the size of array in upRight.
# Each of the next n lines contains a string of two space-separated integers representing coordinates r and c for elements upRight[i].

import math
import os
import random
import re
import sys


#
# Complete the 'countMax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY upRight as parameter.
#


def countMax(upRight):
    # Write your code here
    max = 0
    for corner in up_right:
        corner = list(map(int, corner.split()))
        if corner[0] > max:
            max = corner[0]
        if corner[1] > max:
            max = corner[1]
    grid = [[0 for i in range(max)] for j in range(max)]
    for corner in up_right:
        for i in range(corner[0]):
            for j in range(corner[1]):
                grid[i][j] += 1
    max = 0
    for row in grid:
        for cell in row:
            if cell > max:
                max = cell
    count = 0
    for row in grid:
        for cell in row:
            if cell == max:
                count += 1
    return count
