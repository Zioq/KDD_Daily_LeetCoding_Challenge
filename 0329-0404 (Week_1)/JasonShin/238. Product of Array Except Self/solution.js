//https://leetcode.com/problems/product-of-array-except-self/
//Wednesday submission.
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
    let resultArray = new Array();
    
    // First try that using shift method. And Multiply expcept targetValue. But I got "Time Limit exceeded" 
    // for(let i = 0; i < nums.length; i++){
    //     let currentValue = nums.shift();
    //     resultArray.push(nums.reduce((a,b)=> a*b));
    //     nums.push(currentValue);
    // }
    
    //Here is another solution with two pointers that head right and left directions.
    let leftPointer = 1;
    let rightPointer = 1;
    //goes through right direction and times next element in prev pointer.
    for(let i = 0; i < nums.length; i++){
        resultArray[i] = rightPointer;
        rightPointer *= nums[i];
    }
    
    //one more left direction and multiples next element in prev pointer.
    for(let i = nums.length-1; i>= 0; i--){
        resultArray[i] *= leftPointer;
        leftPointer *= nums[i];
    }
    
    return resultArray;
};