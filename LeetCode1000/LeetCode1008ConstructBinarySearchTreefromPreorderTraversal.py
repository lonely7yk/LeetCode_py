"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left 
has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a 
preorder traversal displays the value of the node first, then traverses node.left, then traverses 
node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree 
with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""

from typing import List
import bisect
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# # Binary Search + DFS: O(nlogn)
# # 找到第一个比 root 大的数，然后分成两组，前一组构造左子树，后一组构造右子树
# class Solution:
#     def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
#         if not preorder: return None

#         idx = bisect.bisect(preorder, preorder[0])
#         root = TreeNode(preorder[0])
#         root.left = self.bstFromPreorder(preorder[1:idx])
#         root.right = self.bstFromPreorder(preorder[idx:])
#         return root


# DFS: O(n)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(dq, bound):
            if not dq or dq[0] > bound: return None

            root = TreeNode(dq.popleft())
            root.left = dfs(dq, root.val)
            root.right = dfs(dq, bound)

            return root

        dq = collections.deque(preorder)
        return dfs(dq, float('inf'))

