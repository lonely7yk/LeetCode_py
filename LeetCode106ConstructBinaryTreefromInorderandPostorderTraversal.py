"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
# 使用切片会增加时间和空间的复杂度
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         def dfs(inorder, postorder):
#             if not inorder: return None
            
#             val = postorder.pop()
#             node = TreeNode(val)
            
#             idx = indexOf(inorder, val)
#             node.right = dfs(inorder[idx + 1:], postorder)
#             node.left = dfs(inorder[:idx], postorder)
            
#             return node
        
#         return dfs(inorder, postorder)
            

# DFS improve
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        valIdxMap = dict()
        for idx, val in enumerate(inorder):
            valIdxMap[val] = idx

        def dfs(inLeft, inRight, postIdx):
            if inLeft > inRight: return None

            currVal = postorder[postIdx]
            node = TreeNode(currVal)
            midIdx = valIdxMap[currVal]

            node.right = dfs(midIdx + 1, inRight, postIdx - 1)
            rightNum = inRight - midIdx     # 右子树的节点个数
            node.left = dfs(inLeft, midIdx - 1, postIdx - rightNum - 1) # postIdx 从 postIdx - rightNum - 1 开始

            return node

        n = len(inorder)
        return dfs(0, n - 1, n - 1)

