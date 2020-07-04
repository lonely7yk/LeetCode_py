"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

# DP: O(n)
# https://leetcode.com/problems/ugly-number-ii/discuss/69364/My-16ms-C%2B%2B-DP-solution-with-short-explanation

# Let me try to explain this using an example. Let's say we have the first 3 ugly 
# numbers 1, 2, 3. What would be the next number? Given the definition, the next number 
# has to be the the smallest number among 2*(1,2,3), 3*(1,2,3), 5*(1,2,3). Obviously, 
# the smallest number is 2 * 1 = 2. But wait, 2 is already in there. So precisely speaking, 
# the next number has to be the the smallest number among all the existing numbers multiplied 
# by 2, 3,5 that isn't in the list already. Now, we can traverse all numbers and maintain a 
# hashset if we want, but it would become O(N^2). Good news is that we can solve this in a 
# DP-like approach. First, we assume there is only one number in the list, which is 1. 
# The next number is Min(2 * 1, 3 * 1, 5 * 1)=2 and it is not in the list. Because we have 
# already considered 2*1 (we move the pointer to its next position, which is 2), now we only 
# need to consider 2 * 2, 3 * 1, 5 * 1 in the next iteration. This way, we don't have to worry 
# about finding a number that is already in the list.
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        idx2, idx3, idx5 = 0, 0, 0
        
        for i in range(n - 1):
            tmp = min(dp[idx2] * 2, dp[idx3] * 3, dp[idx5] * 5)
            dp.append(tmp)
            
            if tmp == dp[idx2] * 2: idx2 += 1
            if tmp == dp[idx3] * 3: idx3 += 1
            if tmp == dp[idx5] * 5: idx5 += 1
                
        return dp[-1]
        
