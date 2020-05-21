"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 
Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

import collections

# Sliding window: O(n)
# 和438一样的思路
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntMap = collections.defaultdict(lambda : 0)

        # s1 中所有字符的个数保存在 cntMap 中
        for c in s1:
            cntMap[c] += 1

        left = 0
        right = 0
        tot = len(s1)   # 完全匹配还需要的字符数

        while right < len(s2):
            c = s2[right]
            if c in cntMap:
                # 只有 map 中的字符个数大于 0，tot 才减1，如果字符个数小于等于0，表示该字符是多余的
                if cntMap[c] > 0:
                    tot -= 1
                cntMap[c] -= 1

            right += 1

            if tot == 0: return True

            if right - left == len(s1):
                c = s2[left]
                if c in cntMap:
                    # 只有 map 中的字符个数大于等于 0，tot 才加1，如果字符个数小于0，
                    # 表示该字符有多余字符，删除当前字符也不会影响 tot
                    if cntMap[c] >= 0:
                        tot += 1
                    cntMap[c] += 1

                left += 1

        return False

# s1 = "ab"
# s2 = "eidbaooo"
s1= "ab"
s2 = "eidboaoo"
res = Solution().checkInclusion(s1, s2)
print(res)