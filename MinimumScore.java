/**
 * You are given a binary array A with elements 0 and 1 of size N, and integer
 * K.
 * Let's call the score of an array the difference between the maximum and
 * minimum element within the array. For example [1,0,0,1,0,0],
 * the Score of this given array is [1-0=1].
 * Now you have to partition the array into K continuous subarrays such that the
 * summation of the score of all the subarrays is minimum. You also have to
 * output starting and ending points of the subarrays corresponding to the
 * minimum score, in increasing order of starting point. If there are multiple
 * possibilities then output the subarrays such that starting points will be
 * lexicographically smallest.
 * 
 * Input format
 * The first line contains two space-separated integers N, and K denoting the
 * size of the array and the number of subarrays in which you have to divide the
 * array respectively.
 * The second line contains N space-separated integers denoting array A.
 * 
 * Output format
 * In the first line print the minimum score.
 * Then print K lines, each line will contain starting and ending points of the
 * subarray.
 * 
 * Constraints
 * 2<=N<=10^6
 * 1<=K<=N
 * 
 * Sample Input
 * 
 * 5 2
 * 0 0 1 0 0 1
 * 
 * Sample Output
 * 1
 * 1 1
 * 2 5
 */

//  uncomment this if you want to read input.
// imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;

class TestClass {
   public static void main(String args[]) throws Exception {

      // Sample code to perform I/O:
      // Use either of these methods for input
      // BufferedReader
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      String name = br.readLine(); // Reading input from STDIN
      System.out.println("Hi, " + name + "."); // Writing output to STDOUT

      // Scanner
      Scanner s = new Scanner(System.in);
      String name2 = s.nextLine(); // Reading input from STDIN
      System.out.println("Hi, " + name2 + "."); // Writing output to STDOUT

      // Write your code here

      int n = s.nextInt();
      int k = s.nextInt();
      int[] a = new int[n];
      for (int i = 0; i < n; i++) {
         for (int j = 0; j < n; j++) {
            a[i] = s.nextInt();
         }
         int sum = 0;
         int min = Integer.MAX_VALUE;
         int max = Integer.MIN_VALUE;
         int count = 0;
         int start = 0;
         int end = 0;
         for (int ai = 0; ai < n; ai++) {
            if (a[ai] == 1) {
               count++;
               if (count == 1) {
                  start = ai;
               }
               end = ai;
            }
            if (count == k) {
               for (int j = start; j <= end; j++) {
                  if (a[j] == 0) {
                     sum++;
                  }
               }
               min = Math.min(min, sum);
               max = Math.max(max, sum);
               sum = 0;
               count = 0;
            }
         }
         System.out.println(min);
         count = 0;

         for (int ai = 0; i < n; i++) {
            if (a[i] == 1) {
               count++;
               if (count == 1) {
                  start = i;
               }
               end = i;
            }
            if (count == k) {
               for (int j = start; j <= end; j++) {
                  if (a[j] == 0) {
                     sum++;
                  }
               }
               if (sum == min) {
                  System.out.println((start + 1) + " " + (end + 1));
               }
               sum = 0;
               count = 0;
            }
         }
         System.out.println(max);
         count = 0;

      }
   }
}
