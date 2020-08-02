"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 16
        self.loadFactor = 0.75
        self.size = 0
        self.data = [[] for i in range(self.cap)]

    def hash(self, key):
        # equals to key % self.cap, because self.cap is the power of 2
        return key & (self.cap - 1)
        
    # double the capacity of the HashSet
    def resize(self):
        self.cap <<= 1
        newData = [[] for i in range(self.cap)]
        
        for bucket in self.data:
            # each num in the bucket will be rehashed, and add to new bucket
            for num in bucket:
                newData[self.hash(num)].append(num)
                
        self.data = newData

    def add(self, key: int) -> None:
        # before adding, check whether you should resize the HashSet
        if self.size > self.cap * self.loadFactor:
            self.resize()
        
        hash_ = self.hash(key)
        # for each num in the bucket, if the key has existed, do not add the key
        for num in self.data[hash_]:
            if num == key: return
            
        self.data[hash_].append(key)
        self.size += 1

    def remove(self, key: int) -> None:
        hash_ = self.hash(key)
        idx = -1
        
        # find the index of the key in the bucket
        for i, num in enumerate(self.data[hash_]):
            if num == key: 
                idx = i
                break
                
        # if idx >= 0, it means the key exists in the bucket. remove it
        if idx >= 0: 
            self.data[hash_].pop(idx)
            self.size -= 1
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_ = self.hash(key)
        
        # iterate the num in the bucket to find the key
        for num in self.data[hash_]:
            if num == key: return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
