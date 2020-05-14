"""
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

 

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]
 

Constraints:

1 <= num <= 10^9
"""

from typing import List
import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num1 = num + 1
        num2 = num + 2

        if num1 % 2 != 0:
            num1, num2 = num2, num1

        res1 = []
        for i in range(int(math.sqrt(num1)), 0, -1):
            if num1 % i == 0:
                res1 = [i, num1 // i]
                break

        res2 = []
        for i in range(int(math.sqrt(num2)), 0, -1):
            if num2 % i == 0:
                res2 = [i, num2 // i]
                break

        if abs(res1[1] - res1[0]) < abs(res2[1] - res2[0]):
            return res1
        else:
            return res2

if __name__ == '__main__':
    num = 999

    res = Solution().closestDivisors(num)
    print(res)