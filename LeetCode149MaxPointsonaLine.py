"""
Given n points on a 2D plane, find the maximum number of points that lie 
on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

NOTE: input types have been changed on April 15, 2019. Please reset to 
default code definition to get new method signature.
"""

from typing import List
import collections

# dict: O(n^2) 72ms 68%
# 对于每个点都和另外的点计算斜率（用dx,dy除以他们的最大公约数表示，直接用 dy/dx 会有精度问题）
# 如果有和当前点相同位置的点，就加在 same 上，对于每一个点都计算某斜率点数最多的个数
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def frac(a, b):
            g = gcd(a, b)
            return a // g, b // g

        if len(points) == 1: return 1
        n = len(points)
        res = 0

        for i in range(n):
            dict_ = collections.defaultdict(lambda: 1)
            dict_['inf'] = 1
            same = 0    # 和 points[i] 重合的点
            first = points[i]
            for j in range(i + 1, n):
                second = points[j]
                if first[0] == second[0] and first[1] == second[1]:
                    same += 1
                elif first[0] == second[0]:
                    dict_['inf'] += 1
                else:
                    slope = frac(second[0] - first[0], second[1] - first[1])
                    dict_[slope] += 1

            res = max(res, max(dict_.values()) + same)
        return res

if __name__ == '__main__':
    # points = [[1,1],[2,2],[3,3]]
    # points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

    points = [[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]
    # points = [[0,0],[94911151,94911150],[94911152,94911151]]
    res = Solution().maxPoints(points)
    print(res)
