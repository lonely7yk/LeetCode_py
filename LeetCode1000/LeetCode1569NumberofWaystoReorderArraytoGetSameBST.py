"""
Given an array nums that represents a permutation of integers from 1 to n. We are going to 
construct a binary search tree (BST) by inserting the elements of nums in order into an 
initially empty BST. Find the number of different ways to reorder nums so that the constructed 
BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a 
right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

Return the number of ways to reorder nums such that the BST formed is identical to the original 
BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other 
ways to reorder nums which will yield the same BST.

Example 2:

Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.

Example 4:

Input: nums = [3,1,2,5,4,6]
Output: 19

Example 5:

Input: nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
Output: 216212978
Explanation: The number of ways to reorder nums to get the same BST is 3216212999. Taking this 
number modulo 10^9 + 7 gives 216212978.

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.
"""

from typing import List
import math

# # DFS: 自己建树
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# class Solution:
#     def numOfWays(self, nums: List[int]) -> int:
#         def comb(n, m):
#             if n < m: return 0
#             return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))

#         # 把 node 添加到 BST 中
#         def addNode(root, node):
#             p = root
#             while True:
#                 if node.val < p.val:
#                     if p.left:
#                         p = p.left
#                     else:
#                         p.left = node
#                         break
#                 else:
#                     if p.right:
#                         p = p.right
#                     else:
#                         p.right = node
#                         break

#         # (node, num) 记录每个 node 下有多少个 node（包括自己）
#         numDict = dict()
#         numDict[None] = 0

#         def countNum(node):
#             if not node: return 0

#             left = countNum(node.left)
#             right = countNum(node.right)
#             numDict[node] = left + right + 1
#             return left + right + 1

#         # 计算一个节点下有多少种不同的排列
#         def dfs(node):
#             if not node: return 1
#             if not node.left and not node.right: return 1

#             # 表示左节点下的排列种数
#             left = dfs(node.left)
#             # 表示右节点下的排列种数
#             right = dfs(node.right)

#             n = numDict[node.left]
#             m = numDict[node.right]

#             # 左右节点下的节点个数一共 n + m，要保证 左节点下的有序，右节点下的有序
#             # 相当于在 n+m 个位置中选取 n 个位置给左节点（或者选 m 个位置给右节点）
#             res = comb(n + m, n) * left * right
#             return res


#         dq = collections.deque(nums)
#         root = TreeNode(dq.popleft())

#         # 生成原始 BST
#         while dq:
#             curr = TreeNode(dq.popleft())
#             addNode(root, curr)

#         # 计算每个节点下的 node 数
#         countNum(root)
#         return (dfs(root) - 1) % (10 ** 9 + 7)    # 最后要减一，减去自身的情况

# DFS: 不需要建树的方法
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def comb(n, k):
            return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

        def dfs(nums):
            if len(nums) <= 2: return 1

            leftNums = [v for v in nums if v < nums[0]]
            rightNums = [v for v in nums if v > nums[0]]
            m, n = len(leftNums), len(rightNums)

            return comb(n + m, n) * dfs(leftNums) * dfs(rightNums)

        return (dfs(nums) - 1) % (10 ** 9 + 7)

