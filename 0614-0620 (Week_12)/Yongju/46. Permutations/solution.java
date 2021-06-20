/**
 * Leetcode 46 Permutations
 * https://leetcode.com/problems/permutations/
 */

import java.util.ArrayList;
import java.util.List;

class Solution {
  public List<List<Integer>> permute(int[] nums) {
      List<Integer> inner = new ArrayList<>();
      List<List<Integer>> result = new ArrayList<>();
      boolean[] used = new boolean[nums.length];
      
      helper(nums, used, inner, result);
      
      return result;
  }
  
  public void helper(int[] nums, boolean[] used, List<Integer> inner, List<List<Integer>> result) {
      
      if (inner.size() == nums.length) {
          result.add(new ArrayList<>(inner)); // Since it is a reference
          return;
      }
      
      for (int i = 0; i < nums.length; ++i) {
          if (!used[i]) {
              // track used indexes
              used[i] = true;
              inner.add(nums[i]);

              helper(nums, used, inner, result);

              used[i] = false;
              inner.remove(inner.size() - 1);
          }
      }
  }
}