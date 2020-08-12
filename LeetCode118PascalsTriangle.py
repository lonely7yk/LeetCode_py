"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        
        res = [[1]]
        for i in range(numRows - 1):
            curr = [1]
            last = res[-1]
            for j in range(len(last) - 1):
                curr.append(last[j] + last[j + 1])
            curr.append(1)
            res.append(curr)
            
        return res
            
        