# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

""" 
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Ex) 1  
Input: root = [1,null,2]
Output: 2

Ex) 2  
Input: root = []
Output: 0

Ex) 3  
Input: root = [0]
Output: 1
 """

# Use recursion to calcualte max level of binary tree
""" 
        1          -> LEVEL 1
    2       19      -> LEVEL 2
           17      -> LEVEL 3

We will do recursion until the node has no child (which means none and it does not contribute to increasing the depth of the tree and therefore it's maximum depth is 0)
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root:TreeNode):
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1

# [EXPLANATION STEP BY STEP]
# self.maxDepth(None) = 0
self. maxDepth(10)
max(self. maxDepth(5), self. maxDepth(19)) + 1 # First recursive call from node 10
max(max(self. maxDepth(None), self. maxDepth(None)) + 1, self. maxDepth(19)) + 1  # Recursive call on node 5 and its expansion
max(1, self. maxDepth(19)) + 1 # Replacing for self. maxDepth(None) = 0 
max(1, max(self. maxDepth(17), self. maxDepth(None)) + 1) + 1 # Recursive call from node 19
max(1, max(self. maxDepth(17), 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0 
max(1, max(max(self. maxDepth(None), self. maxDepth(None)) + 1, 0) + 1) + 1 # Recursive call from node 17
max(1, max(max(0, 0) + 1, 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0
max(1, max(0 + 1, 0) + 1) + 1 # Replacing the inner most max
max(1, 1 + 1) + 1 # Replacing the inner most max
max(1, 2) + 1
2 + 1 # Replacing the inner most max
3