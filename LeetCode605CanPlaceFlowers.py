"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, 
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not 
empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List

# One pass: O(n)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:         
        cnt = 1 # 第一个是 0 的话 cnt 比实际的 0 多 1
        res = 0
        idx = 0
        while idx < len(flowerbed):
            if flowerbed[idx] == 0:
                cnt += 1
            else:
                res += (cnt - 1) // 2
                cnt = 0
            
            idx += 1
            
        cnt += 1    # 最后一个是 0 的话 cnt 比实际的 0 多 1
        res += (cnt - 1) // 2
        return res >= n
        
