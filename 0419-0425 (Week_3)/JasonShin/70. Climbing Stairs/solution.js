// https://leetcode.com/problems/climbing-stairs/
// Tuesday Submission

//First attempt, It failed. >>>Time Limit exceeded
var climbStairs = function(n) {
    
    // Using Fibonacci recursion.
    if(n <= 1){
        return 1;
    }
    //Time Complexity: O(2^n)
    return climbStairs(n-1) + climbStairs(n-2);
};

//Second Attempt with Iteration 
var climbStairs = function(n) {


    let fibo = new Array();
    fibo[0] = 1;
    fibo[1] = 2;
    
    for(let i = 2; i <= n; i++){
        fibo[i] = fibo[i-1] + fibo[i-2];
    }

    //time Complexity: O(n)
    //Space complexity: O(n)
    return fibo[n-1];
};
