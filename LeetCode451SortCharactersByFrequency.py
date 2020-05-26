"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

import collections

# # O(nlogn) 先统计字符频率，然后根据频率倒序排序，然后组合字符串
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         cntMap = collections.defaultdict(lambda : 0)

#         for c in s:
#             cntMap[c] += 1

#         kvList = [[k,v] for k,v in cntMap.items()]
#         kvList.sort(key=lambda x : -x[1])

#         res = ""
#         for k, v in kvList:
#             res += k * v

#         return res

# Bucket Sort: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        cntMap = collections.defaultdict(lambda : 0)
        buckets = [[] for i in range(len(s) + 1)]

        for c in s: cntMap[c] += 1

        for c,cnt in cntMap.items():
            buckets[cnt].append(c)

        res = ""
        for i in range(len(s), 0, -1):
            bucket = buckets[i]
            for c in bucket:
                res += c * i

        return res


s = "tree"
res = Solution().frequencySort(s)
print(res)

