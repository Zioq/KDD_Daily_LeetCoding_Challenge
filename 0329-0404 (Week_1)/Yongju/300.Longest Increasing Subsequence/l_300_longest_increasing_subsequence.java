/**
 * Leetcode, 300.Longest Increasing Subsequence
 * https://leetcode.com/problems/longest-increasing-subsequence/
 */

public class l_300_longest_increasing_subsequence {
  public static int lengthOfLIS(int[] nums) {
      return lengthOfLIS(nums, Integer.MIN_VALUE, 0);
  }

  /**
   * Key: Powerset -> all possible subsets
   *      Find the route: Recursion? -> Memoization? -> Dynamic programming 
   */

   /**
    * Brute Force solution. Needs to be improved
    */
  public static int lengthOfLIS(int[] nums, int prev, int curPos) {
      if (curPos == nums.length) {
          return 0;
      }
      int included = 0;
      if (nums[curPos] > prev) {
          included = 1 + lengthOfLIS(nums, nums[curPos], curPos + 1);
      }
      int notIncluded = lengthOfLIS(nums, prev, curPos + 1);
      return Math.max(included, notIncluded);
  }
}
