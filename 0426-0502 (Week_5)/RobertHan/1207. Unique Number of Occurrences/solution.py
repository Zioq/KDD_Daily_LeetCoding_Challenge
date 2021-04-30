# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

""" 
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Ex1) 
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Ex)2
Input: arr = [1,2]
Output: false
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]):
        dic = {}
        for el in arr:
            dic[el] = dic.get(el,0) +1
        print(dic.values())
        print(set(dic.values()))
        return len(dic.values()) == len(set(dic.values()))
# Time Complexity: O(n) n is lenght of arr
# Space Complexity: O(n) n is for key / n is for value 