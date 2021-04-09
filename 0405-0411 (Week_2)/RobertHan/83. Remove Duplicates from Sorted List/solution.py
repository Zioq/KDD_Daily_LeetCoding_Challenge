# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

''' 
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Ex) 
Input: head = [1,1,2]
Output: [1,2]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head:ListNode):
        if head == None:
            return head
        
        curr = head:
        while curr.next != None:
            if curr.val = curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        # Return linked list
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)