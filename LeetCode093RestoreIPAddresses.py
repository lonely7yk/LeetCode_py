"""
Given a string containing only digits, restore it by returning all possible 
valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

from typing import List

class Solution:
    # DFS backtracking: 32ms 62.86%
    def restoreIpAddresses(self, s: str) -> List[str]:
        def findAddressesDFS(curr, res, num, idx, s):
            """ num 表示ip中第几个数，idx表示字符串中第几位 """
            if idx >= len(s): return

            if num == 4:
                # 如果 0 开头且不是最后一位数，则不能作为结果
                if (s[idx] == '0' and idx != len(s) - 1): return

                tmp = int(s[idx:])
                if 0 <= tmp <= 255:
                    res.append(curr + s[idx:])
                return

            # 如果 0 开头，只能让 0 单独作为 ip 中的一个数
            if s[idx] == '0':
                findAddressesDFS(curr + '0.', res, num + 1, idx + 1, s)
                return

            for i in range(idx, len(s)):
                tmp = int(s[idx:i+1])
                if tmp > 255: break
                findAddressesDFS(curr + s[idx:i+1] + '.', res, num + 1, i + 1, s)

        if len(s) < 4: return []
        curr = ""
        res = []
        findAddressesDFS(curr, res, 1, 0, s)

        return res

    # # iterative: 24ms 97.14%
    # def restoreIpAddresses(self, s: str) -> List[str]:
    #     def isValid(sIp):
    #         tmp = int(sIp)
    #         if (sIp[0] == '0' and len(sIp) > 1) or tmp < 0 or tmp > 255:
    #             return False
    #         return True

    #     n = len(s)
    #     if len(s) < 4: return []

    #     res = []

    #     for i in range(1, 4):       
    #         # [0, i)
    #         if i >= n - 2: break
    #         for j in range(i + 1, i + 4):   
    #             # [i, j)
    #             if j >= n - 1: break
    #             for k in range(j + 1, j + 4):   
    #                 # [j, k)
    #                 if k >= n: break
    #                 s1 = s[:i]
    #                 s2 = s[i:j]
    #                 s3 = s[j:k]
    #                 s4 = s[k:]

    #                 if isValid(s1) and isValid(s2) and isValid(s3) and isValid(s4):
    #                     res.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)

    #     return res


if __name__ == '__main__':
    # s = '0000'
    s = "010010"

    res = Solution().restoreIpAddresses(s)
    print(res)


