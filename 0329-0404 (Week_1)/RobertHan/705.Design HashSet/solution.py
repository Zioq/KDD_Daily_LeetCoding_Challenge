# Design a HashSet without using any built-in hash table libraries.
# https://leetcode.com/problems/design-hashset/

''' Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 '''
class MyHashSet:

    def __init__(self):
        self.numBucket = 10
        self.buckets = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.numBucket)]

    def create_hash(self,key):
        return key % self.numBucket

    def add(self,key):
        i = self.create_hash(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)
    
    def remove(self,key):
        i = self.create_hash(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self,key):
        i = self.create_hash(key)
        if key in self.buckets[i]:
            return True
        else:
            return False

    # If you want to test in you local machine with python 3, uncomment below code.
    ''' def __str__(self):
        return "".join(str(item) for item in self.buckets) '''


obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.add(3)
print(obj)
obj.remove(3)
print(obj)
print("Check the contain",obj.contains(2))