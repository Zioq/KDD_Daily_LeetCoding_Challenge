#https://leetcode.com/problems/move-zeroes/
#283.MoveZeros
#explanation: https://anhyesun.medium.com/learning-python-with-interview-questions-4-move-zeros-dd1a824d1803
class Solution(object):
    def moveZeroes(self, nums):
        slow = 0
        for i in nums:
            if i != 0:
                nums[slow] = i
                slow += 1
        for i in range(slow, len(nums)):
             nums[i] = 0
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
