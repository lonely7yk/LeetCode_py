"""
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

Constraints:

The number of nodes in the tree is in the range [1, 2 * 10^4].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# # DFS
# class Solution:
#     def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
#         def dfs(node, low, high):
#             if not node: return 0
            
#             if node.val < low:
#                 return dfs(node.right, low, high)
#             elif node.val > high:
#                 return dfs(node.left, low, high)
#             else:
#                 return node.val + dfs(node.left, low, high) + dfs(node.right, low, high)
            
#         return dfs(root, low, high)


# Iteration
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    res += node.val
                if node.val >= low:
                    stack.append(node.left)
                if node.val <= high:
                    stack.append(node.right)
                    
        return res
        
