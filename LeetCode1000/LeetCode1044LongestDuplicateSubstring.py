"""
Given a string S, consider all duplicated substrings: (contiguous) substrings 
of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  
(If S does not have a duplicated substring, the answer is "".)

Example 1:

Input: "banana"
Output: "ana"

Example 2:

Input: "abcd"
Output: ""
 

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.

"""

import collections
import functools

# Binary Search + Rabin-Karp: O(nlogn)
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2 ** 63 - 1

        # 通过 Rolling Hash 在字符串中找是否有两个一样的给定长度的子串
        def helper(L):
            p = (26 ** L) % mod
            cur = functools.reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = collections.defaultdict(list)
            seen[cur].append(0) # seen[cur] 表示 hash 值为 cur 的字符串的第一个字符的索引

            # i 表示以 S[i] 结尾
            for i in range(L, len(S)):
                cur = (cur * 26 - A[i - L] * p + A[i]) % mod
                if cur in seen:
                    # 以 S[i] 结尾的字符串
                    subStr1 = S[i - L + 1:i + 1]
                    for idx in seen[cur]:
                        # 和 subStr1 hash 值一致的字符串
                        subStr2 = S[idx:idx + L]
                        if subStr1 == subStr2: return i - L + 1
                seen[cur].append(i - L + 1)

            return -1

        # 二分搜索查找长度范围
        left, right = 0, len(S)
        start, sLen = -1, -1
        while left < right:
            mid = (left + right) // 2
            pos = helper(mid)

            if pos != -1:
                start = pos
                sLen = mid
                left = mid + 1
            else:
                right = mid

        return S[start:start+sLen]



S = "banana"
res = Solution().longestDupSubstring(S)
print(res)


