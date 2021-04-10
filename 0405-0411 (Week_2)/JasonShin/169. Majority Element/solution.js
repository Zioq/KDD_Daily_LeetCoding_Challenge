// https://leetcode.com/problems/majority-element/
//Saturday submission


/**
 * @param {number[]} nums
 * @return {number}
 */
 var majorityElement = function(nums) {
    let majorityPortion = nums.length/2;
    let hashMap = {}
    
    for(let i = 0; i < nums.length; i++) {
        if(!hashMap[nums[i]]){
            hashMap[nums[i]] = new Array();
            hashMap[nums[i]].push(i);
        }else{
            hashMap[nums[i]].push(i);
        }
    }
    
    for(const [key, value] of Object.entries(hashMap)) {
        if(value.length > majorityPortion){
            return key;
        }
    }
    
};