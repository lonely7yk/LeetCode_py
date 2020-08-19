"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


from leetcode_api import deserialize
from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # DFS + HashMap
# # 先用 DFS 求出 target 上面所有节点到 target 的距离，保存到一个 map 中
# # 从根节点出发做 DFS，可以 target 一定在左子树或右子树上
# # 我们把 target 所在的子树定义为 nxt。
# # 现在有三种情况
# # 1. 当前结点到 target 距离大于 K：那么我们只能在 nxt 子树上找结点了，因为在没有 target 的子树上找的结点都会大于当前结点到 target 的距离
# # 2. 当前结点到 target 距离等于 K：我们要把当前结点加到 res 中，然后我们也还是要在 nxt 子树上继续找结点
# # 3. 当前结点到 target 距离小于 K：我们除了在 nxt 子树上找结点，还要在另一个子树上找距离当前结点 K-(当前结点到 target 距离) 的节点
# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
#         # node : distance between node and target (node is above target)
#         distMap = dict()
#
#         # 计算 node 到 target 的距离，保存到 distMap 中
#         def calDist(node, target):
#             if not node: return -1
#             if node.val == target.val:
#                 distMap[node] = 0
#                 return 0
#
#             left = calDist(node.left, target)
#             right = calDist(node.right, target)
#             dist = -1
#             if left != -1:
#                 dist = 1 + left
#             elif right != -1:
#                 dist = 1 + right
#
#             # 只有当 target 在 node 的子孙节点时才保存到 distMap 中
#             if dist != -1: distMap[node] = dist
#             return dist
#
#         # 找到 node 节点子孙中，距离为 dist 的所有节点，保存到 res 中
#         def findAll(node, dist, res):
#             if not node: return
#
#             if dist == 0:
#                 res.append(node.val)
#                 return
#
#             findAll(node.left, dist - 1, res)
#             findAll(node.right, dist - 1, res)
#
#         # 找 node 下面所有距离 target 为 K 的节点（不包括 target 的子孙节点）
#         def dfs(node, res, K):
#             # 只到 target 节点为止
#             if node.val == target.val: return
#             currDist = distMap[node]
#             # nxt 是通向 target 路径上的节点
#             nxt = node.left if node.left in distMap else node.right
#
#             if currDist == K:
#                 res.append(node.val)
#             elif currDist < K:
#                 if node.left in distMap:
#                     findAll(node.right, K - currDist - 1, res)
#                 else:
#                     findAll(node.left, K - currDist - 1, res)
#
#             dfs(nxt, res, K)
#
#         res = []
#         calDist(root, target)
#         dfs(root, res, K)       # 找到不在 target 子节点下的节点
#         findAll(target, K, res) # 找到在 target 子节点下的节点
#         return res


# # 上面方法的精简版，主要的差别在 dfs 方法
# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
#         # node : distance between node and target (node is above target)
#         distMap = dict()
#
#         # 计算 node 到 target 的距离，保存到 distMap 中
#         def calDist(node, target):
#             if not node: return -1
#             if node.val == target.val:
#                 distMap[node] = 0
#                 return 0
#
#             left = calDist(node.left, target)
#             right = calDist(node.right, target)
#             dist = -1
#             if left != -1:
#                 dist = 1 + left
#             elif right != -1:
#                 dist = 1 + right
#
#             # 只有当 target 在 node 的子孙节点时才保存到 distMap 中
#             if dist != -1: distMap[node] = dist
#             return dist
#
#         # 找 node 下面所有距离 target 为 K 的节点
#         def dfs(node, res, length, K):
#             # 只到 target 节点为止
#             if node is None: return
#             # 只有在通向 target 路径的节点上是使用 distMap 中的距离
#             if node in distMap: length = distMap[node]
#             if length == K: res.append(node.val)
#
#             # 其他路径的节点和 target 子孙节点，都相当于在远离 target 节点
#             dfs(node.left, res, length + 1, K)
#             dfs(node.right, res, length + 1, K)
#
#         res = []
#         calDist(root, target)
#         dfs(root, res, distMap[root], K)
#         return res


# DFS + BFS
# DFS 构建 graph
# BFS 计算和 target 距离为 K 的节点
# 应该是最好写的方法
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)

        def buildMap(node):
            if not node: return

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                buildMap(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                buildMap(node.right)

        buildMap(root)
        dq = collections.deque([target.val])
        visited = {target.val}  # 是否访问过

        for i in range(K):
            size = len(dq)

            for j in range(size):
                curr = dq.popleft()

                for nxt in graph[curr]:
                    if nxt not in visited:
                        dq.append(nxt)
                        visited.add(nxt)

        return list(dq)


arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = deserialize(arr)
K = 2
res = Solution().distanceK(root, root.left, K)
print(res)
