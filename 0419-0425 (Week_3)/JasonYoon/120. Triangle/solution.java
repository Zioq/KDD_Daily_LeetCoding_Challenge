// submission for 2021-04-21
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int bottom = triangle.size()-1;
        int[] min = new int[triangle.get(bottom).size()];
        for(int i = 0; i < min.length; i++){
            min[i] = triangle.get(bottom).get(i);
        }
        for(int i = triangle.size()-2 ; i >= 0; i--){
            List list = triangle.get(i);
            for(int j = 0; j < list.size(); j++){
                min[j] = Math.min(min[j], min[j+1]) + (int)list.get(j);
            }
        }
        return min[0];
    }

}
