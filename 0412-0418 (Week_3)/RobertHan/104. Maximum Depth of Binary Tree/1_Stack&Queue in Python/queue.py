# Queue
# Qeue is a linear data structure that stores items in First In First Out (FIFO) manner. 

# To use a queue in Python, use a 'dequeue' library
from collections import deque
queue = deque()

# insert(5)-insert(2)-insert(3)-insert(7)-delete()-insert(1)-insert(4)-delete
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #print FIFO  deque([3, 7, 1, 4])
queue.reverse() # Reverse the queue
print(queue) # deque([4, 1, 7, 3])

# Time complexity: append & popleft -> O(1)
# Queue Space complexity: O(1)

""" 
To initialize queue in Python, using a queue, instead of list, is much better for cost.
If you use a list and select specific element location, this process requires a memrory to save a location, the time compelxity will be required as O(n)

"""