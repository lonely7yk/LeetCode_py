"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:

After flattening the multilevel linked list it becomes:

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 
How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

Constraints:

Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# # DFS: 22%
# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         if not head: return None
        
#         # 将 curr 后面的 flatten，然后返回 flatten 后的 tail
#         def dfs(curr):
#             # 如果 curr.next 和 curr.child 都为空，直接范围 curr，他就是 tail
#             if not curr.next and not curr.child: return curr
#             # 如果 curr.child 为空，返回 curr.next flatten 的 tail
#             if not curr.child: return dfs(curr.next)
            
#             nxt = curr.next
#             tail = dfs(curr.child)
            
#             curr.next = curr.child
#             curr.child.prev = curr
            
#             # 如果 nxt 为空，就不需要把 nxt 连接上 tail
#             if nxt:
#                 tail.next = nxt
#                 nxt.prev = tail
            
#             # 注意要把 child 清空   
#             curr.child = None
#             return dfs(tail)
        
#         dfs(head)
#         return head

# iterative: 74%
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head

        while p:
            # 如果没有 child 直接走下一个节点
            if not p.child:
                p = p.next
                continue

            # 保存 next 和 child 节点
            nxt = p.next
            child = p.child
            p.child = None

            # 将 p 和 child 连起来
            p.next = child
            child.prev = p

            # 如果 nxt 不为空，找到 child 的 tail，然后把 tail 和 nxt 连起来
            if nxt:
                # 找到 child 的尾巴
                tail = child
                while tail.next:
                    tail = tail.next

                tail.next = nxt
                nxt.prev = tail

            p = p.next

        return head



