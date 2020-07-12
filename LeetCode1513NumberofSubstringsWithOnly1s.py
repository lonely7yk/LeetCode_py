"""
Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
Example 4:

Input: s = "000"
Output: 0
 
Constraints:

s[i] == '0' or s[i] == '1'
1 <= s.length <= 10^5
"""

# O(n) 67%
# class Solution:
#     def numSub(self, s: str) -> int:
#         return sum(len(a) * (len(a) + 1) // 2 for a in s.split('0')) % (10 ** 9 + 7)

# O(n) 67%
# 对于一个长度为 n 的连续 1 的字符串，其总个数为 1 + 2 + ... + n
class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        res = 0
        for c in s:
            cnt = cnt + 1 if c == '1' else 0
            res += cnt

        return res % (10 ** 9 + 7)


s = "0110111"
res = Solution().numSub(s)
print(res)
