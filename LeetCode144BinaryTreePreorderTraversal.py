"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # 方法1
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root: return []
        
#         stack = []
#         res = []
        
#         stack.append(root)
        
#         while stack:
#             node = stack.pop()
#             res.append(node.val)
            
#             if node.right: stack.append(node.right)
#             if node.left: stack.append(node.left)
                
#         return res

# 方法2
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        curr = root

        while stack or curr:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left

            node = stack.pop()
            curr = node.right

        return res