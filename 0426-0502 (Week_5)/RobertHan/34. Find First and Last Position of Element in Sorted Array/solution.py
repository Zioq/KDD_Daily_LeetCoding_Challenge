# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

''' 
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity? -> Use Binary Search

Ex1
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Ex2
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Ex3
Input: nums = [], target = 0
Output: [-1,-1]
'''

class Solution:

    def searchRange(self,nums,target):

        result = [-1,-1]
        result[0] = self.firstIndex(nums,target)
        result[1] = self.lastIndex(nums,target)
        return result

    # Find the starting value and need to go to the left most target value in the array
    def firstIndex(self, nums, target):
        index = -1
        low = 0
        high = len(nums) -1

        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                index = mid
                high = mid + 1
            elif nums[mid] > target: # target is on the left side of mid
                high = mid - 1
            elif nums[mid] < target: # target is on the right side of mid
                low = mid +1
        
        return index
    # Find the right most one
    def lastIndex(slef, nums, target):
        index = -1
        low = 0
        high = len(nums) -1

        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                index = mid
                low = mid + 1 
            elif nums[mid] > target:
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
        return index
