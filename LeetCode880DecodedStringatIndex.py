"""
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is 
read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times 
in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the 
decoded string.

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".

Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".

Constraints:

2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
It's guaranteed that K is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.
"""


# # DFS
# class Solution:
#     def decodeAtIndex(self, S: str, K: int) -> str:
#         num = 0
        
#         for c in S:
#             # 不断计算当前 tape 中的字符个数
#             if not c.isdigit():
#                 num += 1
#             else:
#                 num = num * int(c)
                
#             # 如果大于 K
#             if num >= K:
#                 # 如果是字符就直接返回
#                 if not c.isdigit():
#                     return c
#                 # 否则重新计算字符，并用递归重新计算
#                 else:
#                     lastNum = num // int(c)
#                     newK = K % lastNum
#                     return self.decodeAtIndex(S, newK) if newK > 0 else self.decodeAtIndex(S, lastNum)
                
#         return ""
            

# O(n)
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        num = 0
        idx = -1
        
        # 找到第一个比 K 大的位置
        for i, c in enumerate(S):
            if not c.isdigit():
                num += 1
            else:
                num *= int(c)
                
            if num >= K:
                idx = i
                break
                
        # 从后往前不断减小 num，直到 K 能整除 num
        for i in range(idx, -1, -1):
            c = S[i]
            K %= num
            if K == 0 and not c.isdigit():
                return c
            
            if c.isdigit():
                num /= int(c)
            else:
                num -= 1
        
