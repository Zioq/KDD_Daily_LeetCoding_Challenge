// submission for 2021-04-15
class Solution {
    public int fib(int n) {
        int[] fibs = new int[31];
        fibs[0] = 0;
        fibs[1] = 1;
         
        return findfib(n, fibs);
        
    }
    
    public int findfib(int n, int[] fibs){
        if(n == 0)
            return 0;
        if(fibs[n] == 0){
            fibs[n] = findfib(n-1, fibs)+findfib(n-2, fibs);   
        }
        return fibs[n];
    }
}
