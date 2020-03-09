"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

from typing import List

# # BFS: 180ms 50%
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         # 判断括号是否正确
#         def isValid(s):
#             cnt = 0
#             for c in s:
#                 if c == "(":
#                     cnt += 1
#                 elif c == ")":
#                     cnt -= 1
                    
#                 if cnt < 0:
#                     return False
            
#             return cnt == 0
        
#         queue = collections.deque()
#         queue.append(s)
#         set_ = set()
#         found = False
#         res = []
        
#         while queue:
#             first = queue.popleft()
            
#             if isValid(first):
#                 res.append(first)
#                 found = True
                
#             if found: continue
                
#             for i in range(len(first)):
#                 if first[i] == "(" or first[i] == ")":
#                     tmp = first[:i] + first[i+1:]
#                     if tmp not in set_:
#                         queue.append(tmp)
#                         set_.add(tmp)
                
#         return res

# DFS: 32ms 95%
# 先正着删除，然后反着删除，删完以后就是最终结果
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # last_i: 上次遍历的位置的后一个字符的位置
        # last_j: 上次删除的位置的后一个字符的位置
        def dfs(s, res, last_i, last_j, p):
            cnt = 0
            for i in range(last_i, len(s)):
                if s[i] == p[0]: cnt += 1
                if s[i] == p[1]: cnt -= 1

                if cnt >= 0: continue

                # 每次有一个多余 p[1] 括号，就要把它删掉
                for j in range(last_j, i + 1):
                    if j != last_j and s[j] == s[j - 1]: continue # 相同的只删除第一个，防止重复

                    if s[j] == p[1]: 
                        # 这里使用 i,j 而不是 i+1,j+1 是因为有一个字符被删除，所以 i,j 就变成了原字符串
                        # 对应 i+1,j+1 的位置
                        dfs(s[:j] + s[j+1:], res, i, j, p)  
                return  # 因为这次是删过，所以 s 一定不可能加入到 res

            # 通过上面那个循环，说明从左往右没有问题，但是从右往左可能还有问题
            rev = s[::-1]
            # p[0] == "(" 表示现在还是正着删的状态，还要进行一次反着删
            if p[0] == "(": dfs(rev, res, 0, 0, p[::-1])    # 注意 p 也要进行翻转
            else: res.append(rev)

        res = []
        dfs(s, res, 0, 0, ("(", ")"))
        return res

