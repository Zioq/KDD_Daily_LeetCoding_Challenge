# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

""" 
Given the head of a singly linked list, reverse the list, and return the reversed list.

Ex_1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Ex_2
Input: head = [1,2]
Output: [2,1]

Ex_3
Input: head = []
Output: []

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tricky Answer
class Solution:
    def reverseList(self, head:ListNode):
        if head = None:
            return None
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        reverse_list = lst[::-1]

        dummy = ListNode(0)
        curr = dummy
        for v in reverse_list:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next

# Real point of this question(not only for this questions, but other linked list questions): how to manipulate pointer
class Solution:
    def reverseList(self, head:ListNode):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
# Time Complexity: O(n)
# Space Complexity: O(1)