"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
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
        
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        deque = collections.deque()
        res = collections.deque()
        
        deque.append(root)
        
        while deque:
            size = len(deque)
            
            currLevel = []
            for i in range(size):
                node = deque.popleft()
                currLevel.append(node.val)
                
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
                    
            res.appendleft(currLevel)
            
        return res
                
