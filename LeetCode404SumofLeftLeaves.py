"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 
respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS: 24ms 95%
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node, isLeft):
            if not node.left and not node.right and isLeft: return node.val
            
            left = dfs(node.left, True) if node.left else 0
            right = dfs(node.right, False) if node.right else 0
            
            return left + right
        
        if not root: return 0
        return dfs(root, False)
