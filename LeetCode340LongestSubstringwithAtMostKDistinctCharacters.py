"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""


# # Sliding window + HashMap: O(n)   the same idea with LeetCode159
# class Solution:
#     def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#         n = len(s)
#         left, right = 0, 0
#         idxMap = dict()
#         res = 0
        
#         while right < n:
#             c = s[right]
#             idxMap[c] = right
            
#             if len(idxMap) > k:
#                 minIdx = min(idxMap.values())
#                 idxMap.pop(s[minIdx])
#                 left = minIdx + 1
                
#             res = max(res, right - left + 1)
#             right += 1
            
#         return res


# Sliding window + OrderedDict: O(n)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, 0
        idxMap = collections.OrderedDict()
        res = 0
        
        while right < n:
            c = s[right]
            # 如果 c 已经在 idxMap 中了，那么先删除再添加，这样 c 就在 last 的位置了
            if c in idxMap:
                idxMap.pop(c)
            
            idxMap[c] = right
            
            if len(idxMap) > k:
                # 删除第一个，也就是 idx 最小的 c
                _, minIdx = idxMap.popitem(last = False)
                left = minIdx + 1
                
            res = max(res, right - left + 1)
            right += 1
            
        return res
                
