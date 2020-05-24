"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint 
and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x 
with a <= x <= b.  The intersection of two closed intervals is a set of real numbers 
that is either empty, or can be represented as a closed interval.  For example, the 
intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not 
arrays or lists.
 
Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code 
definition to get new method signature.
"""

from typing import List

# Two Pointer : O(m + n)
# class Solution:
#     def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
#         APoint = 0  # 当前 A 的索引
#         BPoint = 0  # 当前 B 的索引
#         res = []

#         while APoint < len(A) and BPoint < len(B):
#             if A[APoint][1] < B[BPoint][0]:
#                 # 表明 A 区间都在 B 区间的前面
#                 APoint += 1
#             elif A[APoint][0] > B[BPoint][1]:
#                 # 表明 A 区间都在 B 区间的后面
#                 BPoint += 1
#             else:
#                 # 表明 A 区间和 B 区间有交集
#                 res.append([max(A[APoint][0], B[BPoint][0]), min(A[APoint][1], B[BPoint][1])])

#                 if APoint + 1 < len(A) and A[APoint + 1][0] <= B[BPoint][1]:
#                     # 表明 A 后一个区间和 B 当前区间有交集
#                     APoint += 1
#                 elif BPoint + 1 < len(B) and A[APoint][1] >= B[BPoint + 1][0]:
#                     # 表明 B 后一个区间和 A 当前区间有交集
#                     BPoint += 1
#                 else:
#                     APoint += 1
#                     BPoint += 1

#         return res

# improved
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []

        while i < len(A) and j < len(B):
            # 如果有交集，就把交集添加在 res 中
            if A[i][0] <= B[j][1] and B[j][0] <= A[i][1]:
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])

            # 判断 A 区间的末尾和 B 区间的末尾大小来决定增加哪个索引
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return res


A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
res = Solution().intervalIntersection(A, B)
print(res)
