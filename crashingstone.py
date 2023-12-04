# crashing stones

# each day a quarry-worker is given a pile of stones and told to reduce the larger stones into smaller ones.
# the worker smash the stones together to reduce them, and is told to always pick up the larger two stones and smash them together.
# if the stone are of equal weight, they both disintegrate entirely. if one is larger, the smaller one is disintegrate and the larger one is reduced by the weight of the smaller one.
# eventually, there is either one stone left that cannot be broken, or all of the stones have been smashed.
# determine the weight of the last stone or return 0 if there is none.

# example 0
# weights = [1,2,3,6,7,7]

# the worker always starts with the two largest stones. in this case, the two largest stones have equal weights of 7 so they both disintegrate when smashed.
# next the worker smashes weight 3 and 6. the smaller one is destroyed and the larger weight 6-3 = 3 units. then, weight 3 and 2 are smashed together, which leaves a stone of weight 1.
# This are no stones left, so the remaining stone weight is 0

# function description
# complete the function lastStoneWeight in the editor below.
# the function must return an integer that denotes the weight of the each stone.

# lastStoneWeight has the following parameter(s):
# int weights[n]: an array of integers indicating the weight of each stones

# constraints
# 1 <= n <= 10^5
# 1 <= weights[i] <= 10^9

# input format for custom testing
# the first line contains an integer n, indicating  the size of array weights.
# each of the next n lines contains an integer weight[i].

# sample case 0
# sample input
# STDIN    Function
# -----    --------
# 3     →  weights[] size n = 3
# 2     →  weights = [2, 4, 5]
# 4
# 5

# sample output
# 1

# explanation
# first the worker takes stones with weight 4 and 5 and crashes them into each other.
# the first one disintegrates completely.
# the second one is reduced to a weight of 1.
# next the worker crashes the stone into the last stone with weight 2.
# the smaller stone disintegrate and the last stone is reduced to a weight of 1.


# Complete the 'lastStoneWeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY weights as parameter.
#


def lastStoneWeight(weights):
    # Write your code here
    if len(weights) == 0:
        return 0
    if len(weights) == 1:
        return weights[0]
    weights.sort()
    while len(weights) > 1:
        if weights[-1] == weights[-2]:
            weights.pop()
            weights.pop()
        else:
            weights[-2] = weights[-1] - weights[-2]
            weights.pop()
            weights.sort()
    if len(weights) == 0:
        return 0
    else:
        return weights[0]

# def lastStoneWeight(weights):
#     # Write your code here
#     weights.sort()
#     while len(weights) > 1:
#         if weights[-1] == weights[-2]:
#             weights.pop()
#             weights.pop()
#         else:
#             weights[-2] = weights[-1] - weights[-2]
#             weights.pop()
#             weights.sort()
#     if len(weights) == 0:
#         return 0
#     else:
#         return weights[0]

# def lastStoneWeight(weights):
#     # Write your code here
#     if len(weights) == 1:
#         return weights[0]
#     if len(weights) == 0:
#         return 0
#     weights.sort()
#     while len(weights) > 1:
#         if weights[-1] == weights[-2]:
#             weights.pop()
#             weights.pop()
#         else:
#             weights[-2] = weights[-1] - weights[-2]
#             weights.pop()
#             weights.sort()
#     if len(weights) == 0:
#         return 0
#     else:
#         return weights[0]