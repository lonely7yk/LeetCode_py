"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer 
should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point 
to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, 
with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# # BFS
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root: return None
#         dq = collections.deque([root])
        
#         while dq:
#             size = len(dq)
#             for i in range(size):
#                 node = dq.popleft()
#                 if i != size - 1: node.next = dq[0]
                
#                 if node.left: dq.append(node.left)
#                 if node.right: dq.append(node.right)
                    
#         return root


# # follow up: DFS
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         # nxtNode 为 node 要连接的 node
#         def dfs(node, nxtNode):
#             if not node: return
            
#             dfs(node.left, node.right)
#             dfs(node.right, nxtNode.left if nxtNode else None)
#             node.next = nxtNode

#         if not root: return None
#         dfs(root, None)
#         return root


# follow up improve: O(1) memory
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        leftmost = root

        while leftmost.left:
            p = leftmost
            while p:
                p.left.next = p.right

                if p.next:
                    p.right.next = p.next.left

                p = p.next

            leftmost = leftmost.left

        return root


