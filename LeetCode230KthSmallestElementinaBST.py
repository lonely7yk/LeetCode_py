"""
Given a binary search tree, write a function kthSmallest to find the kth 
smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need 
to find the kth smallest frequently? How would you optimize the kthSmallest 
routine?
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
    # # DFS(inorder traversal): 56ms 40%
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     def dfs(node, count):
    #         """ inorder traversal """
    #         if not node: return

    #         dfs(node.left, count)
    #         count.append(node.val)
    #         dfs(node.right, count)

    #     count = []
    #     dfs(root, count)
    #     return count[k - 1]

    # DFS + Divide: 64ms 15%
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def countNum(node):
            if not node: return 0

            return countNum(node.left) + countNum(node.right) + 1

        def dfs(node, k):
            leftNum = countNum(node.left)
            if leftNum + 1 == k: return node.val
            elif leftNum + 1 < k: return dfs(node.right, k - leftNum - 1)
            else: return dfs(node.left, k)

        return dfs(root, k)


