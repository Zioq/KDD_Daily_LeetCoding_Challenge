// Submission for Thursday
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        int[] r = {-1, -1};
        while(start <= end){
            int index = end+start/2;
            int element = nums[index];
            if(element == target)
                return findRange(nums, target, index);
            if(element < target)
                start = index+1;
            else 
                end = index-1;
        }
        return r;
    }
    public int[] findRange(int[] nums, int target, int index){
        int start = index;
        int end = index;
        while(start >= 0){
            if(nums[start] == target)
                start--;
            else
                break;
        }
        start++;
        while(end < nums.length){
            if(nums[end] == target)
                end++;
            else
                break;
        }
        end--;
        int[] r = {start, end};
        return r;   
    }
}
