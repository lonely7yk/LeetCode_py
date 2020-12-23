"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS: O(n)    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        memo = {None: 0}
        def dfs(node):
            if not node: return True
            if not node.left and not node.right:
                memo[node] = 1
                return True
            
            left, right = True, True
            if node.left: left = dfs(node.left)
            if node.right: right = dfs(node.right)
                
            memo[node] = max(memo[node.left], memo[node.right]) + 1
            return abs(memo[node.left] - memo[node.right]) <= 1 and left and right
        
        return dfs(root)
            
            
        
