"""
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a 
decreasing relationship between two numbers, 'I' represents an increasing relationship between 
two numbers. And our secret signature was constructed by a special integer array, which contains 
uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). 
For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't 
be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string 
that can't represent the "DI" secret signature.

On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] 
could refer to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where 
the number 1 and 2 construct an increasing relationship.

Example 2:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]

Note:

The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000
"""

from typing import List

# # reverse: O(n) - O(1)
# class Solution:
#     def findPermutation(self, s: str) -> List[int]:
#         # 将 nums 从 left 到 right 中的进行反转
#         def reverse(nums, left, right):
#             while left < right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1
        
#         n = len(s)
#         nums = list(range(1, n + 2))
        
#         i = 0
#         while i < n:
#             # I 表示上升，不需要改动
#             if s[i] == 'I':
#                 i += 1
#             else:
#                 j = i
#                 # 找到递减的范围
#                 while j < n and s[j] == 'D':
#                     j += 1
                    
#                 reverse(nums, i, j)
#                 i = j
                
#         return nums

# Stack: O(n) - O(n)
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = [1]
        res = []
        n = len(s)
        
        for i in range(n):
            # 每当遇到 I，表明升序，把 stack 全部排出放到 res 中
            if s[i] == 'I':
                while stack:
                    res.append(stack.pop())
            # 每个数当要放到 stack 中
            stack.append(i + 2)

                
        while stack:
            res.append(stack.pop())
            
        return res

        
