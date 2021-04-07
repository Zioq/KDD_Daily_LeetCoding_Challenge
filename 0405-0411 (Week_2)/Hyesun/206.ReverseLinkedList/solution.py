#206. Reverse Linked List
#https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        #dead head 2 variables  
        """
        prv = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prv
            prv = cur
            cur = temp
        return prv
        """
        #one variable
        cur = None
        while head:
            temp = head.next
            head.next = cur
            cur = head
            head = temp
        return cur
        """
        :type head: ListNode
        :rtype: ListNode
        """