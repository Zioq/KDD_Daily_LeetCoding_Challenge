//  Submission for Friday
class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        List<Integer> list = new ArrayList<Integer>();
        HashMap<Integer, Boolean> hash = new HashMap<Integer, Boolean>();
        findPower(x, y, bound, list, hash, 0, 0);
        return list;
    }
    public void findPower(int x, int y, int bound, List<Integer> list, HashMap<Integer, Boolean> hash, int i, int j){
        int val = (int)(Math.pow(x, i)+Math.pow(y, j));
        if(val > bound)return;
        if(hash.getOrDefault(val , false) == true){
            findPower(x, y, bound, list, hash, i, j+1);
            return ;
        }
        else if(val <= bound){
            hash.put(val, true);
            list.add(val);            
        }

        else
            return;
        if(x != 1)
            findPower(x, y, bound, list, hash, i+1, j);
        if(y != 1)
            findPower(x, y, bound, list, hash, i, j+1);
    }
}
