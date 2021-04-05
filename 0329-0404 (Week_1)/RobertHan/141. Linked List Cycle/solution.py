# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

''' 
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
 
Ex) 3->2->0->4 
       ^     |
       |_____|      
    Output: True
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head:listNode):
        root = head
        while root:
            # Go forward root node to the end of linst Node
            root = root.next 
            # If root.next is None, which means that this node is last element of linked node and the pointer does not link any other nodes.
            if root.next == None:
                return False
            # else it's means linked other node
            else:
                return True

## Solution using a slow, fast algorithm.
class Solution:
    def hasCycle(self, head:listNode):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


