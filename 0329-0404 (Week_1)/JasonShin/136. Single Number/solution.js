// https://leetcode.com/problems/single-number/
// Thursday Submission.

/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
    if(nums.length === 1){
        return nums[0];
    }
    let map = {};
    
    nums.map((num, index) => {
        if(map[num]){
            map[num].push(index);
        } else {
            map[num] = new Array();
            map[num].push(index);
        }
    })
    
    for (item in map) {
        if(map[item].length === 1){
            return item;
        }
    }
};

//Other solution in discussion board.
//This is using bitwise XOR. 
//Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR
function singleNumber(nums) {
	return nums.reduce((prev, curr) => prev ^ curr);
}