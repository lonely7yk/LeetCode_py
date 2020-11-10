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
    # DFS: 92ms 50% O(n)
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


# # My solution - DFS + memo: O(n) - O(n)
# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         # 找到从这个节点往下的最大长度
#         @functools.lru_cache(None)
#         def findMaxLength(node):
#             if not node: return 0
            
#             if node.val >= 0:
#                 # 如果 node.val >= 0，那直接往下找
#                 return node.val + max(findMaxLength(node.left), findMaxLength(node.right))
#             else:
#                 # 如果 node.val < 0，那么判断下面的长度是否大于 node.val，如果不是则返回 0
#                 left = findMaxLength(node.left)
#                 right = findMaxLength(node.right)
#                 return max(0, node.val + max(left, right))
        
#         # 用 DFS 遍历每一个 node，对于每一个node，计算 findMaxLength(node.left) + findMaxLength(node.right) + node.val，找到其中的最大值
#         def dfs(node):
#             # 这里如果 node 为空，则返回负无穷，这样如果树中没有正数就会返回最大的负数
#             if not node: return float('-inf')
            
#             left = findMaxLength(node.left)
#             right = findMaxLength(node.right)
            
#             return max(left + right + node.val, dfs(node.left), dfs(node.right))
        
#         return dfs(root)
        


if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # root = TreeNode(-3)
    res = Solution().maxPathSum(root)
    print(res)