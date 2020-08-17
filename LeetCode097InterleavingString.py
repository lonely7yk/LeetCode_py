"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""

# # 2D DP: O(mn) - O(mn)
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m = len(s1)
#         n = len(s2)
#         if len(s3) != m + n: return False
        
#         dp = [[False for j in range(n + 1)] for i in range(m + 1)]
#         dp[0][0] = True
        
#         for i in range(1, m + 1):
#             if not dp[i - 1][0]: break
#             dp[i][0] = s1[i - 1] == s3[i - 1]
            
#         for j in range(1, n + 1):
#             if not dp[0][j - 1]: break
#             dp[0][j] = s2[j - 1] == s3[j - 1]
            
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if dp[i][j - 1]:
#                     dp[i][j] |= s2[j - 1] == s3[i + j - 1]
                
#                 if dp[i - 1][j]:
#                     dp[i][j] |= s1[i - 1] == s3[i + j - 1]
                    
#         return dp[-1][-1]
        
# # 1D DP: O(mn) - O(n)
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m = len(s1)
#         n = len(s2)
#         if len(s3) != m + n: return False
        
#         dp = [False for j in range(n + 1)]
        
#         for i in range(m + 1):
#             for j in range(n + 1):
#                 if i == 0 and j == 0:
#                     dp[j] = True
#                 elif i == 0:
#                     dp[j] = dp[j - 1] & (s2[j - 1] == s3[j - 1])
#                 elif j == 0:
#                     dp[j] = dp[j] & (s1[i - 1] == s3[i - 1])
#                 else:
#                     dp[j] = (dp[j - 1] & (s2[j - 1] == s3[i + j - 1])) | (dp[j] & (s1[i - 1] == s3[i + j - 1]))
                    
#         return dp[-1]


# # DFS: O(mn) - O(mn)
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m, n = len(s1), len(s2)
#         memo = [[0 for j in range(n + 1)] for i in range(m + 1)]    # 0 表示未访问，1 表示 True，-1 表示 False

#         # i 表示 s1 中使用字符个数，j 表示 s2 中使用字符个数
#         # 这个函数的意思是，前 i 个 s1 + 前 j 个 s2 已经可以匹配，剩下的 s1 和 s2 是否能匹配 s3 剩下的
#         def dfs(s1, i, s2, j, s3):
#             if memo[i][j] != 0: return True if memo[i][j] == 1 else False
#             # s1 用完了，剩下的只有 s2
#             if i == len(s1): return s2[j:] == s3[i+j:]
#             # s2 用完了，剩下的只有 s1
#             if j == len(s2): return s1[i:] == s3[i+j:]

#             res = False
#             # 如果 s1 下一个字符和 s3 下一个字符相当，用 dfs 看 i+1,j 的情况
#             if s1[i] == s3[i + j]:
#                 res |= dfs(s1, i + 1, s2, j, s3)

#             # 如果 s2 下一个字符和 s3 下一个字符相当，用 dfs 看 i,j+1 的情况
#             if s2[j] == s3[i + j]:
#                 res |= dfs(s1, i, s2, j + 1, s3)

#             memo[i][j] = 1 if res else -1
#             return res

#         return dfs(s1, 0, s2, 0, s3)

# BFS
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        
        dq = collections.deque()
        dq.append((0,0))
        posSet = set()
        posSet.add((0,0))
        
        while dq:
            x, y = dq.popleft()
            if x == m and y == n: return True
            
            if x + 1 <= m and (x + 1, y) not in posSet:
                if s1[x] == s3[x + y]:
                    posSet.add((x + 1, y))
                    dq.append((x + 1, y))
                    
            if y + 1 <= n and (x, y + 1) not in posSet:
                if s2[y] == s3[x + y]:
                    posSet.add((x, y + 1))
                    dq.append((x, y + 1))
            
        return False
        
