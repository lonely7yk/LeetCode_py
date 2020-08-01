"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

from typing import List
import collections

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        distMap = collections.defaultdict(lambda: 0)    # 保存当前节点所有距离的点的个数
        n = len(points)
        res = 0
        
        for i in range(n):
            for j in range(n):
                if i == j: continue

                dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                distMap[dist] += 1

        
            # 对于当前节点，有 cnt 个相同距离的点，从中选两个进行排列，即 A_n^2
            for cnt in distMap.values():
                res += cnt * (cnt - 1)

            # 每次计算完一个节点后要进行清空
            distMap.clear()

        return res
        

points = [[0,0],[1,0],[2,0]]
res = Solution().numberOfBoomerangs(points)
print(res)
