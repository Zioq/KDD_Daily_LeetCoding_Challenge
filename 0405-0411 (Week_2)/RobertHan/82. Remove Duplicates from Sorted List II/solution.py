# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

''' 
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

ex) 1 
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

ex) 2 

Input: head = [1,1,1,2,3]
Output: [2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode):
        duplicated_list = set()
        curr = head
        
        # Iterate list node and add duplicated value in the set
        while curr and curr.next:
            if curr.val = curr.next.val:
                duplicated_list.add(curr.val)
            curr = curr.next
        
        # Iterates to compare List node and publicated_list 
        # if yes, delete the node
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next != None:
            if curr.next.val in duplicated_list:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next

# Time Complexity: O(n)
# Spcae Complexity: O(1)