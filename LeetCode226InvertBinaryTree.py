"""
Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but 
you can’t invert a binary tree on a whiteboard so f*** off.
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
    # DFS(recursive): 24ms 88%
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node.left and not node.right: return node

            left = dfs(node.left) if node.left else None
            right = dfs(node.right) if node.right else None

            node.left = right
            node.right = left

            return node

        if not root: return None
        return dfs(root)

    # # DFS(iterative): 52ms 5.6%
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root: return None
    #     stack = [root]

    #     while stack:
    #         node = stack.pop()
    #         node.left, node.right = node.right, node.left
    #         if node.left: stack.append(node.left)
    #         if node.right: stack.append(node.right)

    #     return root

