"""
Given the root of a binary tree and a node u in the tree, return the nearest node on the same level 
that is to the right of u, or return null if u is the rightmost node in its level.

Example 1:

Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.

Example 2:

Input: root = [3,null,4,2], u = 2
Output: null
Explanation: There are no nodes to the right of 2.

Example 3:

Input: root = [1], u = 1
Output: null

Example 4:

Input: root = [3,4,2,null,null,null,1], u = 4
Output: 2

Constraints:

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^5
All values in the tree are distinct.
u is a node in the binary tree rooted at root.
"""


import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS: O(n)
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if not root: return None
        
        dq = collections.deque([root])
        while dq:
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                if node == u:
                    if i == size - 1: return None
                    else: return dq.popleft()
                    
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
                    
        return None
        
