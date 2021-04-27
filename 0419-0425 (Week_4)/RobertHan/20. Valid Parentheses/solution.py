# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

''' 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Ex 1)
Input: s = "()"
Output: true

Ex 2)
Input: s = "()[]{}"
Output: true

Ex 3)
Input: s = "(]"
Output

Ex 4)
Input: s = "([)]"
Output: false
'''

class Solution:
    def isValid(self, s:str):
        # create a stack
        stack = []

        # create a dictionary to check the str
        dic = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        # iterate str 
        for v in s:
            if v in dic.values(): # if v is open parenthese
                stack.append(v) # add v to stack
            elif stack and dic[p] == stack[-1]: # if stack is not empty and stack's last element is same with one of close parenthese
                stack.pop() # remove the stack's last element
            else:
                return False
        return stack == [] # if stack is empty return True, or return False

# Time complexity: O(n)
# Space complexity: O(1): stack
