"""
Given a string S and a string T, find the minimum window 
in S which will contain all the characters in T in 
complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

1. If there is no such window in S that covers all characters 
in T, return the empty string "".
2. If there is such window, you are guaranteed that there will 
always be only one unique minimum window in S.
"""

import collections

class Solution:
    # # Greedy(mine): O(n) 108ms 79%
    # def minWindow(self, s: str, t: str) -> str:
    #     charCount = dict()
    #     sLen = len(s)
    #     res = s

    #     # 先统计 t 中的字符数量
    #     for c in t:
    #         if c not in charCount:
    #             charCount[c] = 1
    #         else:
    #             charCount[c] += 1

    #     charNum = len(charCount)    # 一共多少个字母

    #     l, r = 0, 0
    #     seen = dict()   # 表示在 s 中看到的对应 charCount 的字符数量

    #     # 先把 r 调到最近地包含 t 的位置
    #     while True:
    #         if charNum == 0: break
    #         if r == len(s): return ""   # 如果 r 走到头还是没让 charNum == 0，说明 s 中不含 t

    #         r += 1
    #         addChar = s[r - 1]
    #         if addChar in charCount:
    #             if addChar not in seen:
    #                 seen[addChar] = 1
    #             else:
    #                 seen[addChar] += 1
    #             if seen[addChar] == charCount[addChar]: # 字母数量满足，charNum--
    #                 charNum -= 1

    #     if r < len(res):
    #         res = s[l:r]

    #     while True:
    #         # 在已经满足的包含 t 的情况下，从开头开始删字符，但是要保证还是包含 t
    #         while l < r:
    #             toRemoveChar = s[l]
    #             if toRemoveChar in seen:    # 如果要删的字符在 seen 中，看它是否影响 window 包含 t，如果影响就直接break
    #                 if seen[toRemoveChar] - 1 < charCount[toRemoveChar]:
    #                     break
    #                 else:                   # 如果不影响就删除该字符
    #                     l += 1
    #                     seen[toRemoveChar] -= 1
    #             else:                       # 如果要删的字符不在 seen 中，直接删除
    #                 l += 1

    #         # 经过删除后的字符串与之前的 res 比较
    #         if r - l < len(res):
    #             res = s[l:r]

    #         if r == sLen: break

    #         # 每次都要添加一个字符，如果添加字符后该字符，seen 中的字符数量比 charCount 中的多，则break
    #         while r < sLen:
    #             r += 1
    #             toAddChar = s[r - 1]
    #             if toAddChar in seen and seen[toAddChar] + 1 >= charCount[toAddChar]:
    #                 seen[toAddChar] += 1
    #                 break

    #     return res

    # Greedy: 136ms 50%
    # 参考：https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        counter = len(t)
        l, r = 0, 0 # current Window
        L, R = 0, len(s) + 1 # minWindow
        while r < len(s):
            # t 中的字符未全消除，则counter--
            if need[s[r]] > 0:
                counter -= 1
            need[s[r]] -= 1
            r += 1

            while counter == 0:
                if r - l < R - L:
                    L, R = l, r
                if need[s[l]] == 0: # 等于 0 的都是本来在 t 中的字符
                    counter += 1
                need[s[l]] += 1
                l += 1

        return "" if R - L == len(s) + 1 else s[L:R]


if __name__ == '__main__':
    S = "ab"
    T = "a"
    res = Solution().minWindow(S, T)
    print(res)