"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each 
element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

from typing import List

# 71%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        flag = 1    # 表示进位

        for i in range(n - 1, -1, -1):
            digits[i] += flag
            flag = digits[i] // 10
            digits[i] %= 10

        if flag == 1:
            digits.insert(0, 1)

        return digits

# # 43%
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n = len(digits)

#         for i in range(n - 1, -1, -1):
#             if digits[i] < 9:
#                 digits[i] += 1
#                 return digits

#             digits[i] = 0

#         digits.insert(0, 1)
#         return digits


digits = [4,3,2,1]
res = Solution().plusOne(digits)
print(res)
