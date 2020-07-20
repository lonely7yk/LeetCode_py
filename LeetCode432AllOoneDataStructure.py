"""
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""

# Double LinkedList
class Node:
    def __init__(self, cnt):
        self.pre = None
        self.next = None
        self.cnt = cnt
        self.keySet = set()

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))

        self.head.next = self.tail
        self.tail.pre = self.head

        self.keyCntDict = dict()
        self.cntNodeDict = dict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keyCntDict:
            self.changeKeyCnt(key, 1)
        else:
            self.keyCntDict[key] = 1
            # 保证有 cnt 为 1 的结点
            if self.head.next.cnt != 1:
                self.addNodeAfter(Node(1), self.head)

            self.head.next.keySet.add(key)
            self.cntNodeDict[1] = self.head.next

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.keyCntDict:
            if self.keyCntDict[key] != 1:
                self.changeKeyCnt(key, -1)
            else:
                self.keyCntDict.pop(key)
                self.removeKeyInNode(self.cntNodeDict[1], key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return list(self.tail.pre.keySet)[0] if self.tail.pre != self.head else ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return list(self.head.next.keySet)[0] if self.tail.pre != self.head else ""
        
    # 修改 key 的 cnt 为 cnt + offset
    def changeKeyCnt(self, key, offset):
        cnt = self.keyCntDict[key]
        self.keyCntDict[key] = cnt + offset
        currNode = self.cntNodeDict[cnt]
        newNode = None

        # 如果新的 cnt 对应的 node 存在直接取
        # 不存在，新建一个 node，如果 offset == 1 添加在 currNode 后面，如果 offset == -1 添加在 currNode.pre 的后面
        if cnt + offset in self.cntNodeDict:
            newNode = self.cntNodeDict[cnt + offset]
        else:
            newNode = Node(cnt + offset)
            self.cntNodeDict[cnt + offset] = newNode
            self.addNodeAfter(newNode, currNode if offset == 1 else currNode.pre)

        newNode.keySet.add(key)
        self.removeKeyInNode(currNode, key)

    # 在 pre 节点后添加 node 节点
    def addNodeAfter(self, node, pre):
        nxt = pre.next
        pre.next = node
        node.pre = pre

        nxt.pre = node
        node.next = nxt

    # 从当前结点的 keySet 中删除 key
    def removeKeyInNode(self, node, key):
        node.keySet.remove(key)
        # 如果 node 的 keySet 为空，删除节点
        if not node.keySet:
            self.removeNode(node)
            self.cntNodeDict.pop(node.cnt)

    # 删除结点
    def removeNode(self, node):
        pre = node.pre
        nxt = node.next

        pre.next = nxt
        nxt.pre = pre
        node.pre = None
        node.next = None

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

obj = AllOne()
obj.inc("hello")
obj.getMaxKey()
obj.getMinKey()