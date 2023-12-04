# simple max difference 

# in securities research an analyst will look at a number of attributes for a stock.
# one analyst would like to keep a record of the highest positive spread between a closing price and the closing price on any prior day in history.
# determine the maximum positive spread for a stock given its price history. if the stock remains flat or declines for the full period, return -1

# example 0 
# px = [7,1,2,5]

# calculate the positive difference between each price and its predecessors: 
# at the first quote, there is no earlier quote to compare to. 
# at the second quote, there was no earlier price that was lower.
# at the third quote, the price is higher than the second quote:2-1=1
# at the fourth quote, the price is higher than the third quote and the second quote:5-2=3 5-1=4
# the maximum difference is 4

# example 1
# px = [7,5,3,1]

# the price declines each quote, so there is never a difference greater than 0. in this case return -1.

# function description
# complete the function maxDifference in the editor below. 
# maxDifference has the following parameters:
# int px[n]: an array of stock prices(quotes)
# returns:
# int: the maximum difference between two prices as described above.

# constraints
# 1<=n<=10^5
# -10^5<=px[i]<=10^5

# sample input 0
# STDIN    Function
# -----    --------
# 7    →   px[] size n = 7
# 2    →   px = [2, 3, 10, 2, 4, 8, 1]
# 3
# 10
# 2
# 4
# 8
# 1

# sample output 0
# 8


def maxDifference(px):
      # Write your code here
      maxD = -1
      for i in range(len(px)):
         for j in range(i+1,len(px)):
               if px[j] - px[i] > maxD:
                  maxD = px[j] - px[i]
      return maxD
      