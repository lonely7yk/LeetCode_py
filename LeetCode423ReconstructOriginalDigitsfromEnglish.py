"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, 
output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means 
invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.

Example 1:
Input: "owoztneoer"

Output: "012"

Example 2:
Input: "fviefuro"

Output: "45"
"""

# O(n)
# https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/91207/one-pass-O(n)-JAVA-Solution-Simple-and-Clear
class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = [0 for i in range(10)]

        for c in s:
            if c == 'z': cnt[0] += 1
            elif c == 'w': cnt[2] += 1
            elif c == 'u': cnt[4] += 1
            elif c == 'x': cnt[6] += 1
            elif c == 'g': cnt[8] += 1
            elif c == 'h': cnt[3] += 1  # 3 - 8
            elif c == 'f': cnt[5] += 1  # 5 - 4
            elif c == 's': cnt[7] += 1  # 7 - 6
            elif c == 'o': cnt[1] += 1  # 1 - 0 - 2 - 4
            elif c == 'i': cnt[9] += 1  # 9 - 8 - 6 - 5

        cnt[3] -= cnt[8]
        cnt[5] -= cnt[4]
        cnt[7] -= cnt[6]
        cnt[1] = cnt[1] - cnt[0] - cnt[2] - cnt[4]
        cnt[9] = cnt[9] - cnt[8] - cnt[6] - cnt[5]

        res = ''

        for i in range(10):
            res += str(i) * cnt[i]

        return res


s = "fviefuro"
res = Solution().originalDigits(s)
print(res)
