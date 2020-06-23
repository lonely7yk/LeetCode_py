"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h 
nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # 直接 DFS 中序遍历: 40%
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         def dfs(node):
#             if not node: return 0
#             return 1 + dfs(node.left) + dfs(node.right)

#         return dfs(root)

# 使用完全二叉树的特性，如果左高度和右高度一直则节点为 2^h - 1，否则用 dfs 计算左右子树及节点个数然后 +1: 96%
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def dfs(node):
            leftPoint, rightPoint = node, node
            leftHeight, rightHeight = 0, 0

            while leftPoint:
                leftHeight += 1
                leftPoint = leftPoint.left

            while rightPoint:
                rightHeight += 1
                rightPoint = rightPoint.right

            if leftHeight == rightHeight: return 2 ** leftHeight - 1
            else: return 1 + dfs(node.left) + dfs(node.right)

        return dfs(root)


