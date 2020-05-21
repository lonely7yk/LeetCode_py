"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:
     1
    / \
   2  3
  /
 4

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
     1
    / \
   2  3
   \   \
   4   5

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
      1
    / \
   2  3
   \
   4    

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # BFS: 队列中保存当前结点和该结点的父节点，如果在同一层找到 x 和 y，且他们的父节点不为同一个结点则返回 true
# class Solution:
#     def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
#         if not root or not root.left or not root.right: return False

#         deque = collections.deque([[root.left, root], [root.right, root]])

#         while deque:
#             n = len(deque)
#             flag = False    # 表示在当前层是否找到 x 或者 y
#             parent = None

#             for i in range(n):
#                 node, curParent = deque.popleft()

#                 if node.val == x or node.val == y:
#                     if not flag:
#                         # 在当前层第一次遇到 x 或者 y，记录下该结点的父节点
#                         flag = True
#                         parent = curParent
#                     else:
#                         # 在第二次遇到 x 或者 y，如果父节点不同，则为true，不然返回false
#                         return curParent != parent

#                 if node.left: deque.append([node.left, node])
#                 if node.right: deque.append([node.right, node])

#             # 如果在当前层遇到过 x 或者 y，但是没有都遇到，则返回 false
#             if flag: return False

#         return False

# BFS: 队列中保存当前结点，对于每一个节点，如果有两个子节点，判断是否就是 x 和 y。这样只要在同一层同时找到 x 和 y 就能返回 True
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        deque = collections.deque([root])

        while deque:
            n = len(deque)
            xFlag = False   # 当前层是否存在 x
            yFlag = False   # 当前层是否存在 y

            for i in range(n):
                node = deque.popleft()
                if node.val == x: xFlag = True
                if node.val == y: yFlag = True
                if xFlag and yFlag: return True     # 如果该层同时存在 x 和 y，由于已经排除同父的情况，所以可以返回 True

                # 排除 x，y 在同一层并共享同一个父节点的情况
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y: 
                        return False

                    if node.left.val == y and node.right.val == x:
                        return False

                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)

            # 如果当前层只有 x 或者 y，但不同时存在，则返回 False
            if xFlag or yFlag: return False

        return False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
res = Solution().isCousins(root, 2, 3)
print(res)


            
