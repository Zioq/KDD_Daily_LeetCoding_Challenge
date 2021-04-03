
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            if sorted(s) == sorted(t):
                return True
            else: 
                return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        explanation: 
        https://anhyesun.medium.com/learning-python-with-interview-questions-2-anagram-fa421eb5c57c
        """
