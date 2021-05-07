# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

''' 
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode):
        if root is None:
            return True
        else:
            return self.search(root.left, root.right)
        
    def search(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        if left.val == right.val:
            inside = self.search(left.right, right.left)
            outside = self.search(left.left, right.right)
            return inside and outside
        else:
            return False
# TC: O(n) where n is node of tree
# SC: O(n) when thee worst case(the height is in O(n)), if the tree is binary tree, then O(log n)
    
        