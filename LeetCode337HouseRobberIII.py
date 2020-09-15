"""
The thief has found himself a new place for his thievery again. There is only one entrance to 
this area, called the "root." Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on 
the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

import functools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DP: 用 lru_cache
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         @functools.lru_cache(None)
#         def dfs(node, canTake):
#             if not node: return 0
            
#             if not canTake:
#                 return dfs(node.left, True) + dfs(node.right, True)
            
#             take = node.val + dfs(node.left, False) + dfs(node.right, False)
#             notTake = dfs(node.left, True) + dfs(node.right, True)
#             return max(take, notTake)
        
#         return dfs(root, True)

# DP: 用 map
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         nodeMap = dict()

#         def dfs(node):
#             if not node: return 0
#             if node in nodeMap: return nodeMap[node]

#             take = node.val
#             if node.left:
#                 take += dfs(node.left.left) + dfs(node.left.right)

#             if node.right:
#                 take += dfs(node.right.left) + dfs(node.right.right)

#             notTake = dfs(node.left) + dfs(node.right)
#             res = max(take, notTake)
#             nodeMap[node] = res

#             return res

#         return dfs(root)


# DP: Best Practice
class Solution:
    def rob(self, root: TreeNode) -> int:
        # 返回一个二元 list，第一个表示取 node 的最大结果，第二个表示不取 node 的最大结果
        def dfs(node):
            if not node: return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            res = []
            res.append(node.val + left[1] + right[1])
            res.append(max(left[0], left[1]) + max(right[0], right[1]))
            return res

        res = dfs(root)
        return max(res[0], res[1])
        
