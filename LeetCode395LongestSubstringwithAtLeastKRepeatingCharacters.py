'''
Find the length of the longest substring T of a given string 
(consists of lowercase letters only) such that every character 
in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times 
and 'b' is repeated 3 times.
'''

class Solution:
    # # 116ms 15.21%
    # def longestSubstring(self, s: str, k: int) -> int:
    #     # 表示 26 个字母前 i 个字符串中有多少个数量
    #     charCnt = [[0 for j in range(len(s) + 1)] for i in range(26)]
    #     for i in range(1, len(s) + 1):
    #         for j in range(26):
    #             c = ord(s[i - 1]) - ord('a')
    #             if c == j:
    #                 charCnt[j][i] = charCnt[j][i - 1] + 1
    #             else:
    #                 charCnt[j][i] = charCnt[j][i - 1]
    #
    #     return self.longestSubString(s, k, 0, len(s) - 1, charCnt)
    #
    # def longestSubString(self, s: str, k: int, left: int, right: int, charCnt: list):
    #     if left > right: return 0
    #
    #     flag = False	# 表示字符串中是否有小于 k 的个数的字符串
    #     splitChar = 'a'
    #
    #     charNum = [0 for i in range(26)]    # 表示从 left 到 right 每个字符的数量
    #     for i in range(26):
    #         charNum[i] = charCnt[i][right + 1] - charCnt[i][left]
    #         if charNum[i] < k and charNum[i] != 0:
    #             flag = True
    #             splitChar = chr(ord('a') + i)
    #
    #     if flag is False:   # 如果所有字符个数都大于 k
    #         return right - left + 1
    #
    #     maxLen = 0
    #     l = left
    #     for i in range(left, right + 1):
    #         if s[i] == splitChar:
    #             maxLen = max(maxLen, self.longestSubString(s, k, l, i - 1, charCnt))
    #             l = i + 1
    #
    #     maxLen = max(maxLen, self.longestSubString(s, k, l, right, charCnt))
    #
    #     return maxLen

    # DFS: 28ms 95.16%
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

if __name__ == '__main__':
    solution = Solution()
    s = "bbaaacbd"
    k = 3
    print(solution.longestSubstring(s, k))