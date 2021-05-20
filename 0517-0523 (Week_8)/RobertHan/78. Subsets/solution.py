# 78. Subsets
# https://leetcode.com/problems/subsets/

''' 
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

'''

class Solution:
    def subsets(self, nums: List[int]):
        output =[[]]
        for n in nums:
            output += [o + [n] for o in output]
        return output

# SC: O(N * 2^N)
# SC: O(N * 2^N)