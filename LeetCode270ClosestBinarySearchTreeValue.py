"""
Given a non-empty binary search tree and a target value, find the value in the BST that is 
closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # Binary Search: recursive
# class Solution:
#     def closestValue(self, root: TreeNode, target: float) -> int:
#         def dfs(node, target):
#             if not node.left and not node.right: return node.val
            
#             if node.val == target: 
#                 return node.val
#             elif node.val < target:
#                 if node.right: 
#                     rightCloestValue = dfs(node.right, target)
#                     return node.val if abs(node.val - target) < abs(rightCloestValue - target) else rightCloestValue
#                 else: 
#                     return node.val
#             else:
#                 if node.left: 
#                     leftCloestValue = dfs(node.left, target)
#                     return node.val if abs(node.val - target) < abs(leftCloestValue - target) else leftCloestValue
#                 else:
#                     return node.val
                
#         return dfs(root, target)

# Binary Search: iterative O(h) - O(1)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        p = root
        res = root.val
        while p:
            # res = min(res, p.val, key=lambda x: abs(target - x))
            if abs(p.val - target) < abs(res - target): res = p.val
            if p.val < target: p = p.right
            else: p = p.left
                
        return res
