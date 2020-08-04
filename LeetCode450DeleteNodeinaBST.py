"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # Recursive: O(h) - O(h)
# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         def findMin(node):
#             while node.left: node = node.left
#             return node
        
#         def dfs(node, key):
#             if not node: return None
#             # key 在左子树上
#             if key < node.val: 
#                 node.left = dfs(node.left, key)
#                 return node
#             # key 在右子树上
#             if key > node.val: 
#                 node.right = dfs(node.right, key)
#                 return node
            
#             # 当前结点是要删除的节点
#             if not node.left: return node.right
#             if not node.right: return node.left
            
#             minNode = findMin(node.right)
#             node.val = minNode.val
#             node.right = dfs(node.right, minNode.val)
#             return node
        
#         return dfs(root, key)

# Iterative: O(h) - O(1)
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 删除一个节点 root，返回删除以后的树的根节点
        def deleteRootNode(root):
            if not root.left: return root.right
            if not root.right: return root.left

            # 找到右子树中最小的节点
            pre, curr = None, root.right
            while curr.left:
                pre = curr
                curr = curr.left

            curr.left = root.left
            if root.right != curr:      # 这种情况 pre != None          
                pre.left = curr.right
                curr.right = root.right

            return curr

        # 找到要删除的节点，和前一个节点
        pre, curr = None, root
        while curr and curr.val != key:
            pre = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right

        # 没有这个节点，直接返回root
        if not curr: return root

        if not pre:
            # 删除的是根节点，直接更新根节点
            root = deleteRootNode(curr)
        else:
            # curr 是 pre 左子树，就更新左子树；是右子树就更新右子树
            if pre.left == curr:
                pre.left = deleteRootNode(curr)
            else:
                pre.right = deleteRootNode(curr)

        return root
