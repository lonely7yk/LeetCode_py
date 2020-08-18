"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same 
structure and node values with a subtree of s. A subtree of s is a tree consists of 
a node in s and all of this node's descendants. The tree s could also be considered 
as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS: O(|s|*|t|)    |s| 为 s 的 node 数
class Solution:
    # 判断两个节点是否结构一致
    def isSameStructure(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        if s.val != t.val: return False
        
        return self.isSameStructure(s.left, t.left) and self.isSameStructure(s.right, t.right)
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s: return False
        if s.val == t.val:  # 当 s.val == t.val 时才进行结构一致判断
            if self.isSameStructure(s, t): return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
        
