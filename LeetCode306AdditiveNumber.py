"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?
"""

# # 用回溯法做的，有点僵硬
# # DFS: 28ms 74%
# class Solution:
#     def isAdditiveNumber(self, num: str) -> bool:
#         def dfs(curr, res, s):
#             if res: return
            
#             if not s and len(curr) >= 3:
#                 res.append(curr)
#                 return
            
#             for i in range(1, len(s) + 1):
#                 if len(curr) < 2:
#                     dfs(curr + [int(s[:i])], res, s[i:])
#                 else:
#                     tmp = int(s[:i])
#                     if tmp == curr[-1] + curr[-2]:
#                         dfs(curr + [tmp], res, s[i:])
                        
#                 if s[0] == "0": break
        
#         res = []
#         dfs([], res, num)
#         return res

# 先找到两个数，pre1 和 pre2，然后在剩下的数中找第三个数，如果找不到就返回 False，继续找 pre1, pre2
# 找到的话继续递归，直到 num 中没有字符。注意找 pre1 的时候只要找到 n//2，因为至少要三个数，最多两个数
# 长度为 n//2。找 pre2 的时候，满足 max(i, j - i) > (n - j) 即可，因为 pre1 和 pre2 的长度都不能
# 超过 pre3。最后，注意一下如果第一位是 '0'，就不继续往下遍历。
# DFS: 20ms 97%
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(pre1, pre2, num):
            if not num: return True

            n = len(num)
            for i in range(1, n + 1):
                curr = int(num[:i])
                if curr == pre1 + pre2:
                    return dfs(pre2, curr, num[i:])
                # 第一个数是 '0' 就不往下遍历
                if num[0] == '0': break

            return False

        n = len(num)
        # 遍历到 n // 2，因为至少要三个数，最多两个数长度为 n//2
        for i in range(1, n // 2 + 1):
            pre1 = int(num[:i])
            
            # 这里不用遍历到 n，因为至少要留一位给第三个数
            for j in range(i + 1, n):
                # 第一位和第二位长度不能比最后以后一位长
                if max(i, j - i) > (n - j): break

                pre2 = int(num[i:j])
                if dfs(pre1, pre2, num[j:]): return True
                # 第一个数是 '0' 就不往下遍历
                if num[i] == '0': break
            # 第一个数是 '0' 就不往下遍历
            if num[0] == '0': break

        return False

num = "199111992"
res = Solution().isAdditiveNumber(num)
print(res)


