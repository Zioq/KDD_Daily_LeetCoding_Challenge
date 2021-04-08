// https://leetcode.com/problems/maximum-subarray/
// Thursday submission

/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    if(nums.length === 1) return nums[0];
    
    let accNum = 0;
    let maxNum = Math.pow(-10,5);
    
    for(let i = 0; i<nums.length; i++){
        accNum = Math.max(accNum + nums[i], nums[i]);
        maxNum = Math.max(accNum, maxNum);
    }
        
    return maxNum;
};