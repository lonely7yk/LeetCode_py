"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.
 
Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Binary Search: O(h) - O(1)
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # 如果 p 有右子树，那结果就是右子树中最左的左子树
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        tmp = root
        res = None

        # 从 root 遍历到 p，最后一个比 p 大的 node 就是结果
        while tmp.val != p.val:
            if tmp.val < p.val:
                tmp = tmp.right
            else:
                res = tmp
                tmp = tmp.left
            
        return res
        
        
