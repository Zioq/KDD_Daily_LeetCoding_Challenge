// https://leetcode.com/problems/move-zeroes/
// Wednesday Submission

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var moveZeroes = function(nums) {
    let counter = 0;
    const numsLength = nums.length;
    
    for(let i = 0; i<numsLength; i++){
        if(nums[i] === 0){
            nums.splice(i, 1);
            i--;
            counter++;
        }
    }
    
    for(let i = 0; i<counter; i++){
        nums.push(0);
    }
};