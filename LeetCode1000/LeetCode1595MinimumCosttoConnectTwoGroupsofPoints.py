"""
You are given two groups of points where the first group has size1 points, the second group has size2 points,
and size1 >= size2.

The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost
of connecting point i of the first group and point j of the second group. The groups are connected if each point in
both groups is connected to one or more points in the opposite group. In other words, each point in the first group
must be connected to at least one point in the second group, and each point in the second group must be connected to
at least one point in the first group.

Return the minimum cost it takes to connect the two groups.

Example 1:

Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.

Example 2:

Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
Output: 4
Explanation: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does
not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.

Example 3:

Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
Output: 10

Constraints:

size1 == cost.length
size2 == cost[i].length
1 <= size1, size2 <= 12
size1 >= size2
0 <= cost[i][j] <= 100
"""

from typing import List
import functools


# DP(DFS+memo)
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        sz1, sz2 = len(cost), len(cost[0])
        minSz2 = [min(cost[i][j] for i in range(sz1)) for j in range(sz2)]  # group2 每个节点连接 group1 的最小 cost

        @functools.lru_cache(None)
        def dfs(idx, mask):
            """
            :param idx: group1 连接完成数量
            :param mask: group2 连接的位上为 1
            :return: 当前 group1 索引为 idx 的节点，在 mask 情况下，连接后的最小结果
            """
            if idx == sz1:
                # 如果 group1 全部完成连接，在 group2 中找还没连接的，取其最小连接 cost
                tmp = 0
                for j in range(sz2):
                    if (mask & (1 << j)) == 0:
                        tmp += minSz2[j]
                return tmp

            res = float('inf')
            for j in range(sz2):
                # 对 group1 中的 idx 节点，尝试连接每一个 group2 中的节点，取其中的最小值
                res = min(res, cost[idx][j] + dfs(idx + 1, mask | (1 << j)))

            return res

        return dfs(0, 0)
