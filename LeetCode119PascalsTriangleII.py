"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

from typing import List

# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         last = [1]
#         for i in range(rowIndex):
#             curr = [1]
#             for j in range(len(last) - 1):
#                 curr.append(last[j] + last[j + 1])
#             curr.append(1)
#             last = curr
            
#         return last


# improved   space complexity: O(k)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0 for i in range(rowIndex + 1)]
        row[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
            
        return row