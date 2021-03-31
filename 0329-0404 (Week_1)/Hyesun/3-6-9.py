#Given an integer n, return a list with each number from 1 to n, except if it's a multiple of 3 or has a 3, 6, or 9 in the number, it should be the string "clap".
#https://binarysearch.com/problems/3-6-9
class Solution: 
    def solve(self, n): 
       ret = []
       for i in range(1, n+1)
           if i % 3 == 0:
              ret.append('clap')
           elif '3' in str(i) or '6' in str(i) or '9' in str(i):
              ret.append('clap')
           else: 
              ret.append(str(i))
       return ret
    
