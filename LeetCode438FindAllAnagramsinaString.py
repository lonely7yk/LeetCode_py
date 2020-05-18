"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will 
not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

from typing import List
import collections

# Sliding window: O(n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pLen = len(p)
        sLen = len(s)
        res = []
        # 表示 p 中每个字符的个数
        cntMap = collections.defaultdict(lambda : 0)

        for c in p:
            cntMap[c] += 1

        left = 0
        right = 0
        tot = pLen # 匹配需要的剩余个数

        # 保证窗口大小为 pLen，当且仅当 tot == 0 时，把 left 加入到结果集中
        while right < sLen:
            c1 = s[right]
            # 如果 c1 在 map 中，每次遇到都要减1（即使小于0）
            if c1 in cntMap:
                # 只有在 c1 个数大于 0 时，tot 才减1，不然就是多余的字符
                if cntMap[c1] > 0:
                    tot -= 1
                cntMap[c1] -= 1
            
            right += 1

            if tot == 0: res.append(left)

            # 一旦 right - left == pLen 说明窗口长度等于 p 长度，这时要把 left 右移一位
            if right - left == pLen:
                c2 = s[left]
                # 如果 c2 在 map 中，每次遇到倒要加1
                if c2 in cntMap:
                    # 只有 c2 个数大于等于 0 时，tot 才加1
                    #（map中的数为复数表明有多余的字符，如果有多余字符，tot就不需要加1）
                    if cntMap[c2] >= 0:
                        tot += 1
                    cntMap[c2] += 1

                left += 1

        return res


s = "abab"
p = "ab"
res = Solution().findAnagrams(s, p)
print(res)
