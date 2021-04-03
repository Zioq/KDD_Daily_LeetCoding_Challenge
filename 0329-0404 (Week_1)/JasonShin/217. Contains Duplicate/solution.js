//https://leetcode.com/problems/contains-duplicate/
//Friday Submission.

/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    if(nums <=1) {
        return false;
    }
 
     for(let i = 0; i < nums.length-1; i++){ 
      for(let j = i+1; j < nums.length; j++){
          if(nums[i] === nums[j]){
              return true;
          }
         }
     }
     
     return false
 };


 //second better solution
 /**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate2 = function(nums) {
    nums.sort();
    for(let i = 0; i < nums.length; i++){
        if(nums[i]===nums[i+1]) return true;
    }
    return false;
 };

 //third solution using Set
 var containsDuplicate3 = function(nums) {
    const setSize = new Set(nums).size;
     if(nums.length !== setSize) return true;
     
     return false
 };