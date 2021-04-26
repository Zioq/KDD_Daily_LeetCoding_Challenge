// Submission for 2021-04-23

class Solution {
    public int countBinarySubstrings(String s) {
        int count = 0;
        int prev = 0, curr = 1;
        for (int i = 1; i < s.length(); i++){
            if(s.charAt(i) == s.charAt(i-1))curr++;
            else{
                prev = curr;
                curr = 1;
            }
            if(prev >= curr)count++;
        }
        return count;
    }

}
