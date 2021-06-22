/**
 * Leetcode 792 Number of Matchig Subsequences
 * https://leetcode.com/problems/number-of-matching-subsequences/
 */

import java.util.HashMap;
import java.util.Map;

class Solution {
  public int numMatchingSubseq(String s, String[] words) {
      int result = 0;
      Map<String, Boolean> map = new HashMap<>();
      
      for (String word: words) {
          if (word.length() > s.length()) continue;    
          
          if (!map.containsKey(word)) {
              if (isSubsequent(s, word)) {
                  map.put(word, true);
                  result++;       
              } else {
                  map.put(word, false);   
              }
          } else {
              if (map.get(word)) result++;
          }
      }        
      
      return result;
  }
  
  public boolean isSubsequent(String s, String word) {
      int wInx = 0;
      for (int i = 0; i < s.length(); ++i) {
          if (word.charAt(wInx) == s.charAt(i)) wInx++;
          if (wInx == word.length()) break;
      }
      return wInx == word.length();
  }
}