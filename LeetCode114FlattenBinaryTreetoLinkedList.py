"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# # DFS: O(n) - O(n)
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         # 把 node 下的节点 flatten 并返回 head（第一个节点） 和 tail（最后一个节点）
#         def dfs(node):
#             if not node.left and not node.right: return node, node
            
#             if not node.left:
#                 head, tail = dfs(node.right)
#                 node.right = head
#                 return node, tail
            
#             if not node.right:
#                 head, tail = dfs(node.left)
#                 node.left = None
#                 node.right = head
#                 return node, tail
            
#             h1, t1 = dfs(node.left)
#             h2, t2 = dfs(node.right)
            
#             node.right = h1
#             node.left = None
#             t1.right = h2
            
#             return node, t2
        
#         if not root: return
#         dfs(root)


# # DFS improve: O(n) - O(n)  上面方法的简略版
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         # flatten node 以下的节点，并返回 tail（最后一个节点）
#         def dfs(node):
#             if not node: return None
#             if not node.left and not node.right: return node
            
#             leftTail = dfs(node.left)
#             rightTail = dfs(node.right)
            
#             if leftTail:
#                 leftTail.right = node.right
#                 node.right = node.left
#                 node.left = None
                
#             return rightTail if rightTail else leftTail
        
#         dfs(root)


# Iterative: O(n) - O(1)
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solution/
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        p = root
        
        while p:
            if p.left:
                rightmost = p.left
                
                while rightmost.right:
                    rightmost = rightmost.right
                    
                rightmost.right = p.right
                p.right = p.left
                p.left = None
                
            p = p.right
        
