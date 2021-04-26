// solution for 2021-04-22
class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        Map<Integer, Integer> map = new HashMap();
        int count = 0;
        for(int i = 0; i < wall.size(); i++){
            List<Integer> list = wall.get(i);
            int sum = 0;
            for(int j = 0; j < list.size()-1; j++){
                sum += list.get(j);
                map.put(sum, map.getOrDefault(sum, 0) + 1);
                count = Math.max(count, map.get(sum));
            }
            
        }
        return wall.size()-count;
    }
}
