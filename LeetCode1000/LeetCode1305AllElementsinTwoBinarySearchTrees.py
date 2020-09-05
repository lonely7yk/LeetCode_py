"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # Inorder Traversal + Merge: O(n)
# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         def dfs(node, arr):
#             if not node: return
            
#             dfs(node.left, arr)
#             arr.append(node.val)
#             dfs(node.right, arr)
            
#         # 用中序遍历把两棵树的所有数都保存到数组中
#         arr1, arr2 = [], []
#         dfs(root1, arr1)
#         dfs(root2, arr2)
        
#         # 把两个有序数组 merge 到一个数组中
#         res = []
#         idx1, idx2 = 0, 0
#         m, n = len(arr1), len(arr2)
#         while idx1 < m and idx2 < n:
#             if arr1[idx1] < arr2[idx2]:
#                 res.append(arr1[idx1])
#                 idx1 += 1
#             else:
#                 res.append(arr2[idx2])
#                 idx2 += 1
                
#         if idx1 < m: res.extend(arr1[idx1:])
#         if idx2 < n: res.extend(arr2[idx2:])
#         return res

# Stack   One-pass: O(n)
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = [], []
        curr1, curr2 = root1, root2
        res = []
        
        while curr1 or curr2 or stack1 or stack2:
            while curr1:
                stack1.append(curr1)
                curr1 = curr1.left
                
            while curr2:
                stack2.append(curr2)
                curr2 = curr2.left
                
            if not stack2 or stack1 and stack1[-1].val < stack2[-1].val:
                node = stack1.pop()
                res.append(node.val)
                curr1 = node.right
            else:
                node = stack2.pop()
                res.append(node.val)
                curr2 = node.right
                
        return res
        
