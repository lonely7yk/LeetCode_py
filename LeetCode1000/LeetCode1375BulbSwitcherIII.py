"""
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.

Example 1:

Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.
Example 2:

Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).
Example 3:

Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.
Example 4:

Input: light = [2,1,4,3,6,5]
Output: 3
Example 5:

Input: light = [1,2,3,4,5,6]
Output: 6 

Constraints:

n == light.length
1 <= n <= 5 * 10^4
light is a permutation of  [1, 2, ..., n]
"""

from typing import List

class Solution:
    # # O(n) O(n): 448ms 12%
    # def numTimesAllBlue(self, light: List[int]) -> int:
    #     maxIdx = 0
    #     set_ = set()
    #     cnt = 0

    #     for l in light:
    #         if l > maxIdx:
    #             for i in range(maxIdx + 1, l):
    #                 set_.add(i)
    #             maxIdx = l

    #         else:
    #             set_.remove(l)

    #         if not set_:
    #             cnt += 1

    #     return cnt

    # O(n) O(1): 452ms 12.5%
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        right = 0   # the most right bulb has been lighted on

        for i, a in enumerate(light, 1):
            right = max(right, a)
            if right == i: res += 1   # 因为 right 是最右边的，right == i 说明前 i 个都被点亮了

        return res


light = [2,1,4,3,6,5]
res = Solution().numTimesAllBlue(light)
print(res)

