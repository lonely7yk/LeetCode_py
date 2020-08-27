"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # BFS: O(nlogn)
# class Solution:
#     def verticalOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: return []
        
#         # (node, col)
#         dq = collections.deque([(root, 0)])
#         nodesMap = collections.defaultdict(list)
        
#         while dq:
#             node, x = dq.popleft()
#             nodesMap[x].append(node.val)
#             if node.left: dq.append((node.left, x - 1))
#             if node.right: dq.append((node.right, x + 1))
            
#         return [tmp[1] for tmp in sorted(nodesMap.items(), key=lambda x: x[0])]
            

# BFS improve: O(n)
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        # (node, col)
        dq = collections.deque([(root, 0)])
        nodesMap = collections.defaultdict(list)
        # 记录最小 col 和最大 col，这样之后就不用排序了
        minCol = 0
        maxCol = 0
        
        while dq:
            node, x = dq.popleft()
            nodesMap[x].append(node.val)
            minCol = min(minCol, x)
            maxCol = max(maxCol, x)

            if node.left: dq.append((node.left, x - 1))
            if node.right: dq.append((node.right, x + 1))
            
        return [nodesMap[i] for i in range(minCol, maxCol + 1)]
