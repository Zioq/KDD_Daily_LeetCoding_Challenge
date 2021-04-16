// submission for 2021-04-16

class Solution {
    public String removeDuplicates(String s, int k) {
        boolean change = true;
        while(change){
            if(s.length() == 0)
                return "";
            StringBuilder sb = new StringBuilder();
            int[] ary = new int[s.length()];
            change = false;
            char prev = s.charAt(0);
            int counter = 1;
            for( int i = 1; i < s.length(); i++){
                char curr = s.charAt(i);
                if(curr == prev){
                    counter++;
                    if(counter == k){
                        change = true;
                        for( int j = 1; j <= k; j++){
                            ary[i-k+j] = 1;
                        }
                    }
                }
                else{
                    counter = 1;
                }
                prev = curr;    
            }
            for( int i = 0; i < ary.length; i++){
                if(ary[i] == 0)
                    sb.append(s.charAt(i));
            }
            s = sb.toString();
        }
        return s;
    }
}
