// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
// Friday Submission

/**
 * @param {number[]} nums
 * @return {number[]}
 */
// 1st solution that use Set
 var findDisappearedNumbers = function(nums) {
    
    nums.sort();
    let setNums = new Set(nums);
    let missingNums = new Array();
    
    for(let i = 1; i<= nums.length; i++){
        if(!setNums.has(i)){
            missingNums.push(i)
        }
    }
    return missingNums;
    //time complexity: O(n)
    //time complexity: O(n)
};

//2nd solution that use built-in filter function for an array
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDisappearedNumbers = function(nums) {
    
    let missingNums = new Array();
    
    for(let i = 1; i <= nums.length; i++) {
        if(nums.filter(num => num === i).length === 0){
            missingNums.push(i)
        }
    }
    
    return missingNums;
    /** 
     * But it is not efficient at all. 
     * Built-in array filter function is O(n) for the time-complexity 
     * Then iteration is O(n).
     * It will be O(n^2) which is terrible solution
     * Space Complexity: O(n)
     * No extra space use.
    */
    
};

//3rd Solution
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDisappearedNumbers = function(nums) {
    
    let missingNums = new Array();
    
    for(let i = 1; i <= nums.length; i++){
        missingNums.push(i);
    }
    
   for(num of nums){
    missingNums[num-1] = -1
   }
    
   return missingNums.filter(num => num !== -1);
   
   /**
    * Time complexity: O(n)
    * space complexity: O(n)
    * No extra space.
    */
};


