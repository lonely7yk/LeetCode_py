"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10
which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

Example 1:

Input: 1
Output: [7]

Example 2:

Input: 2
Output: [8,4]

Example 3:

Input: 3
Output: [8,1,10]

Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
"""

import random


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

def rand7():
    return random.randrange(1, 8)


# # Rejection Sampling
# class Solution:
#     def rand10(self):
#         """
#         :rtype: int
#         """
#         tmp = float('inf')
#
#         while tmp > 40:
#             row = rand7()
#             col = rand7()
#             tmp = (row - 1) * 7 + col
#
#         return (tmp - 1) % 10 + 1

# Rejection Sampling improve: 把 out of range 的数也利用到了
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        tmp = float('inf')

        while True:
            a = rand7()
            b = rand7()
            tmp = b + (a - 1) * 7   # tmp 范围 1-49
            if tmp <= 40:
                return 1 + (tmp - 1) % 10

            a = tmp - 40    # [1,9]
            b = rand7()
            tmp = b + (a - 1) * 7   # tmp 范围 1-63
            if tmp <= 60:
                return 1 + (tmp - 1) % 10

            a = tmp - 60    # [1,3]
            b = rand7()
            tmp = b + (a - 1) * 7   # tmp 范围 1-21
            if tmp <= 20:
                return 1 + (tmp - 1) % 10
