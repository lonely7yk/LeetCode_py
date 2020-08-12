"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each 
letter appears in at most one part, and return a list of integers representing the size of these parts.

 
Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""

from typing import List
import collections

# # No-overlapping: O(nlogn)
# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
#         # key 为 char，value 为一个 list，存储所有 char 出现在字符串中的索引
#         charIdxMap = collections.defaultdict(list)
        
#         for i, c in enumerate(S):
#             charIdxMap[c].append(i)
            
#         # 把每个字符串的出现范围作为区间放入到一个 list 中
#         intervals = []
#         for list_ in charIdxMap.values():
#             intervals.append((list_[0], list_[-1]))
                
#         res = []
#         intervals.sort(key=lambda x: x[0])  # 按照区间的 start 排序
#         currStart = intervals[0][0]
#         currEnd = intervals[0][1]
        
#         # 每一个 part 本质是相连的 interval
#         for i in range(1, len(intervals)):
#             if intervals[i][0] >= currEnd:
#                 res.append(currEnd - currStart + 1)
#                 currStart = intervals[i][0]
                
#             # 每次都要更新 currEnd
#             currEnd = max(currEnd, intervals[i][1])
                
#         # 添加最后一个 interval
#         res.append(currEnd - currStart + 1)
#         return res
        
# Greedy: O(n)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIdx = {c: i for i, c in enumerate(S)}
        start = end = 0
        res = []

        for i, c in enumerate(S):
            end = max(end, lastIdx[c])
            if i == end:    # 如果 end 就是当前索引，说明 start~end 中所有字母的 lastIdx 都不超过 end
                res.append(end - start + 1)
                start = i + 1

        return res

