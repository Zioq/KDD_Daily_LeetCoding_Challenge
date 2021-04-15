# Stack
""" 
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only.
"""

stack = []
# Insert(5)-Insert(2)-Insert(3)-Insert(7)-Delete()-Insert(1)-Insert(4)-Delete()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# Print stack from top to bottom
print(stack[::-1]) #[1,3,2,5]

# Print stack from bottom to top
print(stack()) # [5,2,3,1]
