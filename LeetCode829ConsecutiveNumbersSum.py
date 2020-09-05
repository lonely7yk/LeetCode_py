"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive 
integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3

Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""

# O(N ^ 0.5)
# reference: https://leetcode.com/problems/consecutive-numbers-sum/discuss/129015/5-lines-C%2B%2B-solution-with-detailed-mathematical-explanation.
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        cnt = 0
        upper = int((2 * N + 0.25) ** 0.5 - 0.5) + 1
        
        for k in range(1, upper):
            if (N - k * (k - 1) // 2) % k == 0:
                cnt += 1
                
        return cnt
        
