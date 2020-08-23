"""
Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n.
A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1]
and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction
(See the first example).

Example 1:

Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are
visited only once.

Example 2:

Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
Output: [2]
Example 3:

Input: n = 7, rounds = [1,3,5,7]
Output: [1,2,3,4,5,6,7]

Constraints:

2 <= n <= 100
1 <= m <= 100
rounds.length == m + 1
1 <= rounds[i] <= n
rounds[i] != rounds[i + 1] for 0 <= i < m
"""

from typing import List
import collections

# # brute force：从初始位置一步步走到终点，记录经过位置的次数
# class Solution:
#     def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
#         # 记录每个位置经过的次数（0-indexed）
#         cntMap = collections.defaultdict(lambda: 0)
#         curr = rounds[0] - 1    # 开始位置
#         cntMap[curr] += 1       # 开始位置先 + 1
#
#         for num in rounds:
#             # 在到达当前位置前一直 +1
#             while curr != num - 1:
#                 curr = (curr + 1) % n
#                 cntMap[curr] += 1
#
#         # 按照次数从大到小排序（其次按照位置排序）
#         tmp = sorted(cntMap.items(), key=lambda x: (-x[1], x[0]))
#         # 最大次数
#         max_ = tmp[0][1]
#
#         res = []
#         for x in tmp:
#             if x[1] == max_:
#                 res.append(x[0] + 1)
#
#         return res

# Lee 哥的方法，真的牛逼
# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/discuss/806814/JavaC%2B%2BPython-From-Start-to-End
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[0] <= rounds[-1]:
            return list(range(rounds[0], rounds[-1] + 1))
        else:
            return list(range(1, rounds[-1] + 1)) + list(range(rounds[0], n + 1))


n = 2
rounds = [2,1,2,1,2,1,2,1,2]

# n = 7
# rounds = [1,3,5,7]
res = Solution().mostVisited(n, rounds)
print(res)
