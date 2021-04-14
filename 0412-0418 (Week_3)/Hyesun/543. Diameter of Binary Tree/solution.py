# https://leetcode.com/problems/diameter-of-binary-tree/
# 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        
        def longestPath(node):
            if not node:
                return 0
            nonlocal diameter 
            left, right = longestPath(node.left), longestPath(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
            
        longestPath(root)
        return diameter
        