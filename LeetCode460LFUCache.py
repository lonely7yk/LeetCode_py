"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem,
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since
it was inserted. This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

import collections


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoubledLinkedList:
    def __init__(self):
        self.size = 0

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return self.size

    # 在 DLL 头部插入节点
    def add(self, node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

        self.size += 1

    # 删除节点 node，如果 node 为 None，删除尾部节点
    def pop(self, node=None):
        if self.size == 0: return None

        if not node:
            node = self.tail.prev

        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        node.next = node.prev = None

        self.size -= 1
        return node


# DLL + 2HashMap
# 相同 freq 的都存储在一个 dll 中，dll 是按照 least recent 存储的，头结点是 least recent node
class LFUCache:

    def __init__(self, capacity: int):
        # freq : DoubledLinkedList
        self.freqMap = collections.defaultdict(DoubledLinkedList)
        # key : Node
        self.nodeMap = dict()

        self.minFreq = 0
        self.capacity = capacity
        self.size = 0

    # 更新 node，让 node 频率 +1，从原来的 dll 中删除，添加到新的 dll 中
    # 发生在：1. get(key)       key 在 nodeMap 中
    #        2. put(key, value)  key 在 nodeMap 中
    def _update(self, node):
        freq = node.freq
        oldDll = self.freqMap[freq]
        oldDll.pop(node)

        node.freq += 1
        newDll = self.freqMap[freq + 1]
        newDll.add(node)

        # oldDll 就是最小频率的队列，且 oldDll 现在没有节点了，更新 minFreq
        if self.minFreq == freq and not oldDll:
            self.minFreq = freq + 1

    def get(self, key: int) -> int:
        if key not in self.nodeMap: return -1

        node = self.nodeMap[key]
        self._update(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            self._update(node)
            node.value = value
        else:
            # 如果 size 达到 capacity，先删除最小频率 dll 中的尾节点（表示最晚访问）
            if self.size == self.capacity:
                minFreqDll = self.freqMap[self.minFreq]
                # 从 dll 中删除 least recent node
                popNode = minFreqDll.pop()
                # 从 nodeMap 中删除对应 key 的 entry
                if popNode: self.nodeMap.pop(popNode.key)
                self.size -= 1

            # 添加新 node，更新 minFreq 为 1
            node = Node(key, value)
            self.nodeMap[key] = node
            self.freqMap[1].add(node)
            self.minFreq = 1
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
print(cache.get(3))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))