"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25

Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026

Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
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
    # # DFS: 24ms 95%
    # def sumNumbers(self, root: TreeNode) -> int:
    #     def dfs(node):
    #         """ 返回的是从该结点往下的所有 str 型的结果 list """
    #         if not node.left and not node.right:
    #             return [str(node.val)]

    #         left = dfs(node.left) if node.left else []
    #         right = dfs(node.right) if node.right else []

    #         return [str(node.val) + tmp for tmp in left] + [str(node.val) + tmp for tmp in right]

    #     if not root: return 0
    #     return sum([int(val) for val in dfs(root)])

    # DFS: 28ms 81%
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, val):
            if not node.left and not node.right: return val * 10 + node.val

            left = dfs(node.left, val * 10 + node.val) if node.left else 0
            right = dfs(node.right, val * 10 + node.val) if node.right else 0

            return left + right

        if not root: return 0
        return dfs(root, 0)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    res = Solution().sumNumbers(root)
    print(res)
