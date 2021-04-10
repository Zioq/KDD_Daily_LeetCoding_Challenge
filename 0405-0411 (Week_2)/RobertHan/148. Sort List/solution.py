# 148. Sort List
# https://leetcode.com/problems/sort-list/
''' 
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Ex) 1 
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Ex) 2
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Ex) 3
Input: head = []
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# easiest approach but cheating (Break the Space Complexity)
# This way is add an each of element of linked list into array, and sort the array.
class Solution:
    def sortList(self, head: ListNode):
        curr = head
        lst = []
        while curr:
            lst.appned(curr.val)
            curr = curr.next
        # Sort the array
        sorted_list = lst.sort()

        # Create a new Linked List and add elch of element as an node
        dummy = ListNode(0)
        curr = dummy
        
        # Break the Space Complexity Rule 
        for v in lst:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next


# Use Bubble Sort: which is allow us to use a `constance space complexity`
# The this is break the Space complexity: bubble sort space complexity: O(n^2)
class Solution:
    def sortList(self, head: ListNode):
        n = 0   # We need to know how many times we iterates 
        curr = head
        while curr:
            n +=1
            curr = curr.next
        
        # n nest loop 
        i = 0 # iterater value to track where we are
        while i < n:
            j = 0 
            curr = head
            while j < n-i and curr.next:
                if curr.val > curr.next.val:
                    cur.val, curr.next.val = curr.next.val = cur.val # Change the node value itselft, instead of rebuilding a list node
                    curr = curr.next
                j += 1
            i += 1

        return head
        