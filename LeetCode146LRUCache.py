"""
Design and implement a data structure for Least Recently Used (LRU)
 cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key
if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not
already present. When the cache reached its capacity, it should
invalidate the least recently used item before inserting a new
item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
import collections


class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

# DoubleLinkedList: 212ms 61%
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedNode(0, 0)
        self.tail = LinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.nodeMap = {}

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        else:
            node = self.nodeMap[key]
            self.remove(node)
            self.add(node)
            return self.nodeMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])

        node = LinkedNode(key, value)
        self.nodeMap[key] = node
        self.add(node)
        if len(self.nodeMap) > self.capacity:
            n = self.tail.pre
            self.nodeMap.pop(n.key)
            self.remove(n)

    def add(self, node):
        first = self.head.next

        node.next = first
        first.pre = node

        self.head.next = node
        node.pre = self.head

    def remove(self, node):
        p = node.pre
        n = node.next

        p.next = n
        n.pre = p

# # OrderedDict
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.dict = collections.OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.dict:
#             return -1
#         else:
#             self.dict.move_to_end(key, last=True)
#             return self.dict[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.dict:
#             self.dict.pop(key)
#
#         self.dict[key] = value
#         if len(self.dict) > self.cap:
#             self.dict.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
