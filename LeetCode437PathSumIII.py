"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # Brute Force DFS: 14%
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         def pathSumFrom(node, target):
#             if not node: return 0
#             currNum = 1 if node.val == target else 0
#             return currNum + pathSumFrom(node.left, target - node.val) + pathSumFrom(node.right, target - node.val)
#
#         if not root: return 0
#         return pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


# HashMap + DFS: 78%
# 这道题其实还是挺难的！
# preSumCnt 的 key 是从 root 到之前遍历过节点的 sum，value 是一个有多少个这样的 sum（可能存在多条从根节点出发的路径，导致和为 sum）
# currSum 表示 root 到当前结点的总和，要找到路径为 target，其实可以找 root 出发的路径和有多少条和为 currSum - target 的路径；然后继续向下遍历
# 由于使用的是 DFS，每次遍历到一个节点，preSumCut 存储的都是只有一条路径上的和，所有 preSumCnt[currSum - target] 可以表明到目前位置有多少条从 root 出发的路径和为 currSum - target
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node, currSum, target, preSumCnt):
            if not node: return 0

            currSum += node.val
            # 先找 currSum - target 一共的路径数量
            res = preSumCnt[currSum - target]
            # 把当前的 currSum 添加到 map 中
            preSumCnt[currSum] += 1

            # 继续用 DFS 向下找
            res += dfs(node.left, currSum, target, preSumCnt) + dfs(node.right, currSum, target, preSumCnt)

            # 当前层遍历结束，删掉当前层的 currSum
            preSumCnt[currSum] -= 1
            return res


        # key: 从 root 到之前遍历过某一个节点之间的所有节点的和    value: 对于一个 sum 有多少种从根节点出发的路径
        preSumCnt = collections.defaultdict(lambda: 0)
        # 初始化 sum=0 时有一条路径，表明如果从根节点到某一节点的和正好等于 target 时的情况
        preSumCnt[0] = 1
        return dfs(root, 0, sum, preSumCnt)



# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(11)
# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(-2)
# root.left.right.right = TreeNode(1)
# sum = 8

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
root.right.right.right.right = TreeNode(5)
sum = 3

res = Solution().pathSum(root, sum)
print(res)

