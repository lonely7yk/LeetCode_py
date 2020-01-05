"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some 
starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through 
the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
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
    # DFS: 92ms 50%
    # maxSinglePath(node) = max(0, maxSinglePath(node.left), maxSinglePath(node.right)) + node.val
    # maxPathSum(node) = max(0, maxSinglePath(node.left)) + max(0, maxSinglePath(node.right)) + node.val
    def __init__(self):
        # 这题不需要用字典，因为每个节点只会被调用一次
        # self.singlePathDict = {}
        self.res = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSinglePath(root)
        return self.res

    def maxSinglePath(self, node):
        """ 计算从这个节点往下走的最长 path """
        if not node: return 0

        l = max(0, self.maxSinglePath(node.left))
        r = max(0, self.maxSinglePath(node.right))

        self.res = max(self.res, l + r + node.val)
        return max(l, r) + node.val

if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # root = TreeNode(-3)
    res = Solution().maxPathSum(root)
    print(res)