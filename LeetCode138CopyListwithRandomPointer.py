"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p = head
        d = {}
        d[None] = None  # None 一定对应 None
        
        while p:
            node = None

            # 对于每一个 p（原链表中的节点），在 map 中找是否存在 clone 节点
            # 如果存在，直接取；如果不存在，新建一个，并放入 map
            if p in d:
                node = d[p]
            else:
                node = Node(head.val)
                d[p] = node
                
            # p.next 和 p.random 同理
            if p.next in d:
                node.next = d[p.next]
            else:
                node.next = Node(p.next.val)
                d[p.next] = node.next
                
            if p.random in d:
                node.random = d[p.random]
            else:
                node.random = Node(p.random.val)
                d[p.random] = node.random
                
            p = p.next
            
        return d[head]
                    
            
        
