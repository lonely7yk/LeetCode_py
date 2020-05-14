"""
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Inorder traversal + DFS: 380ms 100%
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def dfs(node):
            if node is None: return

            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        def build(nums):
            if not nums: return None

            n = len(nums)
            mid = n // 2
            node = TreeNode(nums[mid])
            left = build(nums[:mid])
            right = build(nums[mid + 1:])
            node.left = left
            node.right = right
            return node

        dfs(root)
        return build(nums)
