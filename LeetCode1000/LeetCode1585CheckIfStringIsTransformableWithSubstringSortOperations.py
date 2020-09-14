"""
Given two strings s and t, you want to transform string s into string t using the following operation any number of times:

Choose a non-empty substring in s and sort it in-place so the characters are in ascending order.
For example, applying the operation on the underlined substring in "14234" results in "12344".

Return true if it is possible to transform string s into string t. Otherwise, return false.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following sort operations:
"84532" (from index 2 to 3) -> "84352"

"84352" (from index 0 to 2) -> "34852"
Example 2:

Input: s = "34521", t = "23415"
Output: true
Explanation: You can transform s into t using the following sort operations:
"34521" -> "23451"
"23451" -> "23415"

Example 3:

Input: s = "12345", t = "12435"
Output: false

Example 4:

Input: s = "1", t = "2"
Output: false

Constraints:

s.length == t.length
1 <= s.length <= 105
s and t only contain digits from '0' to '9'.
"""

import collections

# 变换后，一个数前面比他大的数的个数一定小于等于变化前，因为排序后小的数不会变到大的数前面

# 先获取 t 中每个数的 count 快照，每遇到一次添加一次快照
# 对于 s 中的每个数 i 的 count2 快照，count2 中比 i 大的数的个数一定要大于 count 中对应的数的个数
# O(n) - O(n)
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # s 和 t 长度不同直接 return False
        if len(s) != len(t): return False

        n = len(s)
        # 记录 t 中的各个数字的个数
        count = [0 for i in range(10)]
        preMap = collections.defaultdict(collections.deque)

        for i in range(n):
            num = int(t[i])
            count[num] += 1
            # 对于每一个数依次添加当时的 count 快照
            preMap[num].append(list(count))

        # 记录 s 中的各个数字的个数
        count2 = [0 for i in range(10)]
        for i in range(n):
            # s 中当前数，要保证 num 前面比 num 大的数的个数都不小于变化后
            num = int(s[i])
            count2[num] += 1

            if preMap[num]:
                curCount = preMap[num].popleft()
                for j in range(num + 1, 10):
                    if count2[j] < curCount[j]: return False

        # 如果 s 和 t 的 count 不一致返回 False
        for i in range(10):
            if count[i] != count2[i]: return False

        return True
