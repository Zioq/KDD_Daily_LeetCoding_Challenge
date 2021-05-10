# 109. Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
''' 
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

 '''

 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode):
        
        new_list = []
        while head != None:
            new_list.append(head.val)
            head = head.next
        
        return self.constructTree(new_list, 0, len(new_list)-1)
    
    def constructTree(self, nums, left, right):
        if left > right:
            return None
        
        midPoint = (left+right) // 2
        
        root = TreeNode(nums[midPoint])
        root.left = self.constructTree(nums, left, midPoint-1)
        root.right = self.constructTree(nums, midPoint+1, right)
        return root
        
# TC: O(N)
# SC: O(N), n is for array 