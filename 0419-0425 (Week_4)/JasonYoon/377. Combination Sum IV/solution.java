// Submission for 2021-04-19

class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target+1];
        for(int i = 1; i < dp.length; i++){
            dp[i] = -1;
        }
        dp[0] = 1;
        return combination(nums, target, dp);
    }
    
    public int combination(int[] nums, int target, int[] dp){
        if(dp[target]!=-1)
            return dp[target];
        
        int val = 0;
        for( int i = 0; i < nums.length; i++){
            if(target >= nums[i]){
                val += combination(nums, target-nums[i], dp);
            } 
        }
        dp[target] = val;
        return val;
    }
}
