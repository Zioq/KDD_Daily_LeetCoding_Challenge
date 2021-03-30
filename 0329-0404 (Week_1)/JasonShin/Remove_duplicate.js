//https://leetcode.com/problems/remove-duplicates-from-sorted-array/
//Monday Submission.
/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
    //check the array has just one or non value.
    if(nums.length <= 1){
        return nums.length;
    }
    //initial pointer.
    var pointer = 0;
    
    while(pointer < nums.length-1){
        if(nums[pointer] === nums[pointer+1]){
            nums.splice(pointer,1);
        }
        else pointer++;
    }
    
    return nums.length;
};