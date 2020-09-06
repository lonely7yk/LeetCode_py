"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character,
the costs of deleting other characters will not change.

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.

Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").

Constraints:

s.length == cost.length
1 <= s.length, cost.length <= 10^5
1 <= cost[i] <= 10^4
s contains only lowercase English letters.
"""

from typing import List


# Greedy: O(n) - O(1)
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        idx = 0
        n = len(s)
        res = 0

        while idx < n:
            start = idx         # 当前起始位置
            curSum = cost[idx]  # 当前重复序列的代价总和
            maxCost = cost[idx] # 当前重复序列的代价最高值

            # 遍历到最后一个重复的字符
            while idx < n - 1 and s[idx] == s[idx + 1]:
                idx += 1
                curSum += cost[idx]
                maxCost = max(maxCost, cost[idx])

            # start == idx 说明只有一个重复字符，就不需要删除
            if start != idx:
                res += curSum - maxCost

            idx += 1

        return res
