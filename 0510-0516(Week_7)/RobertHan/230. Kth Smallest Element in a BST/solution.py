# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

""" 
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        self.counter = 1
        self.k_smallest = None

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            if self.counter == k:
                self.k_smallest = node.val
            self.counter += 1
            inorder(node.right)

        inorder(root)

        return self.k_smallest;

# Recursive In-Order Traversal TC: O(N)