# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' # O(n), 2 paths
        s = s.replace(" ", "").lower()
        alOnly =''
        for st in s:
            if st.isalnum():
                alOnly += st
                
        start = 0
        end = len(alOnly) - 1 
        while (start < end):
            if alOnly[start] != alOnly[end]:
                return False
            start+=1
            end-=1
            
        return True
        '''
        
        start = 0
        end = len(s) -1
        while start < end:
            #consecutive whitespace, non alnum case 
            if not s[start].isalnum() or s[start] == ' ' : 
                start+=1
            elif not s[end].isalnum() or s[end] == ' ': 
                end-=1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start +=1
                    end -=1
        return True