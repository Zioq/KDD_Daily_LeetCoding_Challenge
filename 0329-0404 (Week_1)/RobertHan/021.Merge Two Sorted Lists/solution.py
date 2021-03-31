# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

''' 
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

ex)
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        # Initialize dummy and temp
        # dummy is a flag at the start of the linked list
        # temp is a flag which is going to move forware find which value should be added
        dummy = temp = ListNode(0)

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                tmep.next = l2
                l2 = l2.next
            # Move move forward
            temp = temp.next
        # Adds whatever left to the temp.next 
        temp.next = l1 or l2
        # Return dummy.next because dummy is poiting to `0` and `next` to zero is what we've added throught the process
        return dummy.next

''' 
Time Complexity: O(a+b)
Space Complexity: O(1)
'''
