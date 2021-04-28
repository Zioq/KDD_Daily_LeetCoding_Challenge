// Submission for Tuesday

class Solution {
    public boolean isPowerOfThree(int n) {
        if(n <= 0)
            return false;
        double d = Math.log10(n) / Math.log10(3);
        if(d % 1 == 0)
            return true;
        return false;
    }
}
