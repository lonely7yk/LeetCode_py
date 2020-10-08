"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if 
A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""

# # O(n^2)
# class Solution:
#     def rotateString(self, A: str, B: str) -> bool:
#         if len(A) != len(B): return False
#         if not A: return True
        
#         n = len(A)
#         firstChar = A[0]
#         start = 0
        
#         while True:
#             # 找 B 中第一个出现 A 中第一个字符的字符位置
#             idx = B.find(firstChar, start)
#             # 找不到直接 break
#             if idx == -1: break
            
#             # 从 idx 到 n 的长度
#             m = n - idx
#             if A[:m] == B[idx:] and A[m:] == B[:idx]: return True
#             else: start = idx + 1   # 找不到从 idx 后一个开始查找
            
#         return False
        

# KMP: O(n)
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if not A: return True

        # calculate the nxt array
        n = len(A)
        nxt = [0 for i in range(n)]
        j, i = 0, 1

        while i < n:
            if A[i] == A[j]:
                nxt[i] = j + 1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = nxt[j - 1]
                else:
                    nxt[i] = 0
                    i += 1

        # match the pattern: A in B+B
        s = B + B
        i, j = 0, 0
        while i < 2 * n:
            if s[i] != A[j]:
                if j != 0:
                    j = nxt[j - 1]
                else:
                    i += 1
            else:
                i += 1
                j += 1

                if j == n: return True

        return False

