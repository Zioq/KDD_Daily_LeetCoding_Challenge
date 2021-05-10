# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

'''

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

        0
    -3     9
 -10      5  


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        if (len(nums) == 0 ):
            return None
        
        return self.constructTree(nums, 0, len(nums)-1)
    
    def constructTree(self, nums, left, right):
        if left > right:
            return None
        
        midPoint = (left+right) // 2
        
        root = TreeNode(nums[midPoint])
        root.left = self.constructTree(nums, left, midPoint-1)
        root.right = self.constructTree(nums, midPoint+1, right)
        return root

#TC: O(N)
#SC: O(N)