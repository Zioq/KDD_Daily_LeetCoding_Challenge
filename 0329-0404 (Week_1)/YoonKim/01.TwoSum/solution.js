var twoSum = function(nums, target) {
    let result = [];
    for (let i = 0; i < nums.length; i++) {   
        const firstNum = nums[i]
        for (let a = i+1; a < nums.length; a++){
            if(firstNum + nums[a] === target){
                result.push(i,a);
            }
        }
    }    
    return result;
}


