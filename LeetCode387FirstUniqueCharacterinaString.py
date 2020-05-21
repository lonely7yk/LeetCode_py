"""
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

import collections

# HashMap: O(n) two-pass
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         if not s: return -1

#         n = len(s)
#         idxMap = dict()

#         for i in range(len(s)):
#             c = s[i]
#             if c not in idxMap:
#                 idxMap[c] = i # 如果 c 未出现过，把 c 的索引保存下来
#             else:
#                 idxMap[c] = n # 如果 c 已经出现过，则设为 len(s)

#         res = min(idxMap.values())
#         return res if res != n else -1 

# OrderedDict: O(n) one-pass
# 虽然是 one-pass，但速度其实没有直接用 hashmap 快
class Solution:
    def firstUniqChar(self, s: str) -> int:
        idxMap = collections.OrderedDict()
        charSet = set()

        for i in range(len(s)):
            c = s[i]
            if c in charSet:
                if c in idxMap:
                    idxMap.pop(c)
            else:
                idxMap[c] = i
                charSet.add(c)

        # 找到第一个添加进 idxMap 且没有被删除的
        return idxMap[next(iter(idxMap))] if len(idxMap) > 0 else -1



s = "leetcode"
res = Solution().firstUniqChar(s)
print(res)
