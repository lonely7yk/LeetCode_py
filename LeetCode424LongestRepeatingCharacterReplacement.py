"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

import collections

# # Sliding window: 22%
# # 维持一个滑动窗口，使得窗口中最多字符数加上 k 小于等于窗口大小，看窗口最大能达到多少，就是结果
# # 本质就是找一个滑动窗口，使得窗口大小 >= maxCount + k
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         start, end = 0, 0   # 窗口的 start 和 end 的索引
#         maxCount = 0        # 窗口中最多的字符的个数
#         res = 0
#         cnt = collections.defaultdict(lambda: 0)    # 记录窗口中字符出现的次数
        
#         for c in s:
#             cnt[c] += 1
#             maxCount = max(maxCount, cnt[c])    # 计算窗口中最多字符数

#             # 保证最多字符数 + k <= 窗口长度
#             while end - start + 1 > maxCount + k:
#                 # start 左移一位，把对应的 cnt 减一
#                 cnt[s[start]] -= 1
#                 start += 1
                
#                 # 更新 maxCount
#                 maxCount = max(cnt.values())
                
#             # 现在 窗口大小是满足条件的，更新 res
#             res = max(res, end - start + 1)
#             end += 1    # 每次遍历 end 右移一位
            
#         return res

# Sliding Window improved: 33%
# 滑动窗口只扩大不缩小，maxCount 表示当目前位置滑动窗口中最多的字符数
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        maxCount = 0
        res = 0
        cnt = collections.defaultdict(lambda: 0)

        for c in s:
            cnt[c] += 1
            maxCount = max(maxCount, cnt[c])

            while end - start + 1 > maxCount + k:
                cnt[s[start]] -= 1
                start += 1

            res = max(res, end - start + 1)
            end += 1

        return res

        
s = "ABAA"
k = 0
res = Solution().characterReplacement(s, k)
print(res)

