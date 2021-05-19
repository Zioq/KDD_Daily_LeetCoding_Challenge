# 1. Two Sum
# https://leetcode.com/problems/two-sum/
''' 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Ex1 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Ex2

Input: nums = [3,2,4], target = 6
Output: [1,2]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

 '''

''' First Solution: Double for loop(Brute Force) -> O(N^2) N squre '''
class Solution:
    def twoSum(self, nums:List[int], target:int):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i,j])

''' 
Second Solution: HashMap
 '''

class Solution:
    def twoSum(self, nums:List[int], target:int):
        prevMap = {} # val : index

        for i,n enumerate(nums):
            diff = target - n
            if diff in prevMap: # if difference exists in the hashmap
                return [prevMap[diff], i]
            # if diff is not exists in the hashmap, update it
            prevMap[n]=i
        return 
''' 
TC: O(N), where N is number of element in array
SC: O(N), where N is number of element in array
 '''