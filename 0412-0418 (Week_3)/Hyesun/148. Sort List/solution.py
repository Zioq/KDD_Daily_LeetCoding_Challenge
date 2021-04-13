#148. Sort List
#https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        heap = []
        curr = head
        # push to heap
        while curr:
            heapq.heappush(heap, (curr.val))
            curr = curr.next
        # add dead head
        dum = ListNode(0)
        cur = dum 
        # pop heap and add to new LinkedList
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return dum.next