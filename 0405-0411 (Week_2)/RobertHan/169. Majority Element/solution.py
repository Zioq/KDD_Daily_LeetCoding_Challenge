# 169. Majority Element
# https://leetcode.com/problems/majority-element/

''' 
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


ex)1 
Input: nums = [3,2,3]
Output: 3

ex) 2
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 '''

 class Solution:
        def majorityElement(self, nums: List[int]) -> int:
        bound = len(nums) / 2
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) +1
        for key, val in dic.items():
            if val > bound:
                return key

# Time Complexity: O(n)
# Space Complexity: 