#136. Single Number
#https://leetcode.com/problems/single-number/
#List approach and Bit manipulation approach
class Solution(object):
    def singleNumber(self, nums):
        # numset = []
        # for n in nums: 
        #     if n not in numset:
        #         numset.append(n)
        #     else: 
        #         numset.remove(n)
        # return numset.pop()
        ret = 0
        for i in nums: 
            ret ^= i
        return ret
        """
        :type nums: List[int]
        :rtype: int
        """