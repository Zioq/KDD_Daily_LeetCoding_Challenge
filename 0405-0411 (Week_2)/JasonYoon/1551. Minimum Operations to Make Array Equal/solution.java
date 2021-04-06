// Submission for 2021-04-06
class Solution {
    public int minOperations(int n) {
        int count = 0;
        int middle = (2+(n-1)*2)/2;

        middle--;
        while(middle > 0){
            count += middle;
            middle -= 2;   
        }

        return count;
    }
}
