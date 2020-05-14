"""
Given a positive integer num, write a function which returns True if num is a perfect square 
else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

# O(logn) : 二分法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num + 1

        while left < right:
            mid = (left + right) // 2
            if mid * mid > num:
                right = mid
            elif mid * mid < num:
                left = mid + 1
            else:
                return True

        return False

num = 14
res = Solution().isPerfectSquare(num)
print(res)
