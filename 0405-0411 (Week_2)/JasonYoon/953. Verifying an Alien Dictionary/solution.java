// Submission for 2021-04-09

class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        for(int i = 0 ; i < words.length-1; i++){
            String first = words[i];
            String second = words[i+1];
            int index = 0;
            if(first.equals(second)){}
            else {
                while(index < first.length() && index < second.length()){
                   int fi = order.indexOf(first.charAt(index));
                 int si = order.indexOf(second.charAt(index));
                  if(fi < si)
                      // this will break the while loop
                       index = 21;
                 else if(fi > si)
                     return false;    
                 else if(index == second.length()-1)
                     return false;
                 index++;
            }                
            }

        }
        return true;
    }
}
