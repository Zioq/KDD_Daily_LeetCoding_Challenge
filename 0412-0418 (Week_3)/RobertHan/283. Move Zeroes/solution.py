# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

""" 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Ex) 1
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Ex) 2
Input: nums = [0]
Output: [0]
"""

class Solution:
    def moveZeroes(self, nums: List[int]):
    """ 
    Do not return anything, modify nums in-place instead.
    """
        for v in nums:
            if v == 0:
                nums.remove(v)
                nums.appned(v)

# Instead of add or delete, use swap

class Solution:
    def moveZeroes(self, nums: List[int]):
            """ 
            Do not return anything, modify nums in-place instead.
             """
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
    # Time Complexity: O(n)
    # Space Complexity: O(1)



