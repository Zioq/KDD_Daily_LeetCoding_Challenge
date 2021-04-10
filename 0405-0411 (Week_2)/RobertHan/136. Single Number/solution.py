# 136. Single Number
# https://leetcode.com/problems/single-number/
"""  
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

"""
from collections import defaultdict

class Solution:
    def singleNumber(self, nums:List[int]):
        # Use another list 
        no_duplicated_num = []
        # Iterate over all the elements in nums
        # If some numbers in nums is new to array, append it
        # If some numbers is already in the array, remove it
        for i in nums:
            if i not in no_duplicated_num:
                no_duplicated_num.append(i)
            else:
                no_duplicated_num.remove(i)
        # return only left element
        return no_duplicated_num.pop() 
    # singleNumber runtime-> Time complexity: O(n^2), Space complexity: O(n) 


    def singleNumber2(self,nums:List[int]):
        # Use dictionary
        dic = {}
        for i in nums:
            # if the element in the dic, add +1 or get 0
            dic[i] = dic.get(i,0) +1
        for key, val in dic.items():
            if val ==1:
                return key
    # singleNumber2 runtime -> Time complexity: O(n*1) = O(n) 
    # For loop -> O(n), dictionary in python -> O(1) 
    # Space Complexity -> O(n) The space required by dictionary is equal to the number of element in nums

    def singleNumber3(self, nums:List[int]):
        # Use Hash table 
        hash_table = defaultdict(int)

        # Set the dictionary
        for i in nums:
            hash_table[i] +=1 
        
        # iterate hash_table 
        for i in hash_table:
            if hash_table[i] ==1:
                return i
    
    # singleNumber3 runtime -> Time complexity: O(n*1) = O(n) 
    # For loop -> O(n), hash_table in python -> O(1) 
    # Space Complexity -> O(n) The space required by hash_table is equal to the number of element in nums