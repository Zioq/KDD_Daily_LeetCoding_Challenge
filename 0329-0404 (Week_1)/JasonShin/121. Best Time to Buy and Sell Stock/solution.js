//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
//Tuesday submission.

/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    if(prices.length <= 1){
        return 0;
    }
    let minimum = Math.pow(10,4);
    let diff = 0;
    
    for(const price of prices){
        if(price < minimum) minimum = price;
        else {
            diff = Math.max(diff, price - minimum);
        }
    }
    
    return diff;
};