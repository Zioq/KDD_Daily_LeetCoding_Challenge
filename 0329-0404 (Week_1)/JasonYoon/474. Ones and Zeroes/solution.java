// Submission for 2021-04-02
class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m+1][n+1];
        for(int k = 0; k < strs.length; k++){
            int[] neededCount = new int[2];
            for(int j = 0; j < strs[k].length(); j++){
                neededCount[strs[k].charAt(j)-'0']++;
            }
            for(int i = m; i >= 0; i--)
                for(int j = n; j >= 0; j--)
                    if(i >= neededCount[0] && j >= neededCount[1])
                        dp[i][j] = Math.max(1 + dp[i - neededCount[0]][j - neededCount[1]], dp[i][j]);
            }
        return dp[m][n];
    }
}
