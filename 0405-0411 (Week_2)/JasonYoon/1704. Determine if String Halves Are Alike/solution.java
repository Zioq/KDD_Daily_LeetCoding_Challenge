// Submission for 2021-04-07

class Solution {
    public boolean halvesAreAlike(String s) {
        int balance = 0;
        for( int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(isVowel(c)){
                if(i < s.length()/2)
                    balance++;
                else 
                    balance--;
            }
        }
        return (balance == 0);
    }
    
    public boolean isVowel(char c){
        c = Character.toLowerCase(c);
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            return true;
        return false;
    }
}
