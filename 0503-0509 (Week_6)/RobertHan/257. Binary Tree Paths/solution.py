# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
''' 
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]


Input: root = [1]
Output: ["1"]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root:TreeNode):
        path = []
        if root is None:
            return []
        
        self.search_path(root, '', path)
        return path

    def search_path(self, root, string, path):
        string += str(root.val)

        if root.left:
            self.search_path(root.left, string+'->', path)
        if root.right:
            self.search_path(root.right, string+'->', path)
        if root.left == None and root.right == None:
            path.append(string)
