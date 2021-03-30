#https://binarysearch.com/problems/Length-of-a-Linked-List
''' 
Given a singly linked list node, return its length. The linked list has fields next and val. 

Example
- Input
node =  [5,4,3,]

- Output 
3
'''
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self,node):
        c = 0
        while node:
            c +=1
            node = node.next
        return c

### Explanation ###
''' 
Traversing the linked list till next element is null.
Traverse through the given linked list, keep count of number until the loop terminates.
Time Complexity: O(n) (Because we travel N lenght of Linked list)
Space Complexity: O(1) (Becuase we only take an extra int variable)
 '''