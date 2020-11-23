"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""


# # Sliding Window: O(n)
# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         n = len(s)
#         left, right = 0, 0
#         counter = dict()    # 记录窗口内每个单词的出现次数
#         res = 0
        
#         while right < n:
#             c = s[right]
#             # c 在 counter 中，直接自增
#             if c in counter:
#                 counter[c] += 1
#             # c 不在 counter 中
#             else:
#                 # 如果 counter 中的单词已经等于 2 了
#                 if len(counter) == 2:
#                     # left 不断左移，知道 counter 中只有一个单词
#                     while len(counter) == 2:
#                         counter[s[left]] -= 1
#                         if counter[s[left]] == 0:
#                             counter.pop(s[left])
#                         left += 1
                
#                 counter[c] = 1
                        
#             res = max(res, right - left + 1)
#             right += 1
            
#         return res


# Sliding Window improve: O(n)
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        idxMap = dict()     # 保存字母 c 最后一次出现的索引
        res = 0
        
        while right < n:
            c = s[right]
            idxMap[c] = right
            # 如果 idxMap 长度大于 2
            if len(idxMap) > 2:
                # 找到最小索引对应的字母
                minIdx = min(idxMap.values())
                # 从 map 中删除字母，并更新 left
                idxMap.pop(s[minIdx])
                left = minIdx + 1
                        
            res = max(res, right - left + 1)
            right += 1
            
        return res
