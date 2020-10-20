"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:


Input: root = [2,1,1]
Output: [[1]]

Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""

import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def dfs(node, serialMap, res):
            if not node: return 'N'
            serial = str(node.val) + '#' + dfs(node.left, serialMap, res) + '#' + dfs(node.right, serialMap, res)
            if serialMap[serial] == 1: res.append(node)
            serialMap[serial] += 1
            return serial
            
        serialMap = collections.defaultdict(lambda: 0)
        res = []
        dfs(root, serialMap, res)
        return res
        