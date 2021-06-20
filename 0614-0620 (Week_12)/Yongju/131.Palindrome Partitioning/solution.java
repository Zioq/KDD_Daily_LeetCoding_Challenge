import java.util.ArrayList;
import java.util.List;

class Solution {
  public List<List<String>> partition(String s) {
      List<List<String>> result = new ArrayList<>();
      List<String> inner = new ArrayList<>();
      helper(s, 0, inner, result);
      
      return result;
  }
  
  public void helper(String s, int position, List<String> inner, List<List<String>> result) {
      if (position == s.length()) result.add(new ArrayList<>(inner)); // Since we use reference, inner should be copied
      else
          for (int i = position; i < s.length(); ++i) {
              if (isPalindrome(s, position, i)) {
                  inner.add(s.substring(position, i + 1));
                  helper(s, i + 1, inner, result);
                  inner.remove(inner.size() - 1);  // Revert to previous stack
              }
          }
  }
  
  private boolean isPalindrome(String s, int start, int end) {
      while (start < end) {
          if (s.charAt(start) != s.charAt(end)) return false;
          start++;
          end--;
      }
      return true;
  }
}