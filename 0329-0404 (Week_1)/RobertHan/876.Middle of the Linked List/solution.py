# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

''' 
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
 '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode):
        # If the linked list has at least two nodes
        if(head.next != None):
            temp = head
            count = 0
            while(temp):
                count +=1
                temp = temp.next
            # Find a middle point of linked list
            middle = (count // 2) +1
            # Flag goes forward to the middle point
            c = 0
            while head is not None:
                head= head.next
                c +=1
                if (c == middle-1):
                    return head  
        # If the Linked list has only head, return head
        else:
            return head

# Another Solution using a two pointer(slow, fast)

class Solution:
    def middleNode(self, head: ListNode):
        # head for one step iteration.
        # temp for two step iteration.
        # when the temp reaches the end of the list, the head just reaches the half ot it. 
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head