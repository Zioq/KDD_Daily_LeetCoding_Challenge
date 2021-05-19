# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''  
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.


Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Input: numbers = [2,3,4], target = 6
Output: [1,3]
'''

''' Solution 1: Two Pointers '''

class Solution:
    def twoSum(self, numbers: List[int], target: int):
        l = 0
        r = len(numbers) -1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l +=1
            elif numbers[l] + numbers[r] > target:
                r -=1
            else:
                return [l+1,r+1]
# TC: O(N) 
# SC: O(1)


'''  Solution 2: Dictionary '''
class Solution: 
    def twoSum2(self, numbers: List[int], target: int):
        dic = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in dic:
                return [dic[diff]+1, i+1]
            dic[num] = i
# TC: O(N) 
# SC: O(N)
                
        