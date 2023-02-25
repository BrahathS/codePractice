// Median of Two Sorted Arrays in java

class Solution {
   public double findMedianSortedArrays(int[] num1, int[] num2) {
      int n = num1.length;
      int m = num2.length;
      if (n > m) {
         return findMedianSortedArrays(num2, num1);
      }
      int low = 0;
      int high = n;
      while (low <= high) {
         int partitionX = (low + high) / 2;
         int partitionY = (n + m + 1) / 2 - partitionX;
         int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : num1[partitionX - 1];
         int minRightX = (partitionX == n) ? Integer.MAX_VALUE : num1[partitionX];
         int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : num2[partitionY - 1];
         int minRightY = (partitionY == m) ? Integer.MAX_VALUE : num2[partitionY];
         if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((n + m) % 2 == 0) {
               return ((double) Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
            } else {
               return (double) Math.max(maxLeftX, maxLeftY);
            }
         } else if (maxLeftX > minRightY) {
            high = partitionX - 1;
         } else {
            low = partitionX + 1;
         }
      }
      throw new IllegalArgumentException();
   }
}