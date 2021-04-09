# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

''' 
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

ex)
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []

Input: head = [7,7,7,7], val = 7
Output: []

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head:ListNode, val:int):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next != None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)