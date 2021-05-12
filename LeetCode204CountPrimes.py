"""
Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 
Constraints:

0 <= n <= 5 * 10^6
"""


# # Sieve of Eratosthenes: O(n)
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 1: return 0
        
#         notPrimes = set()
#         res = 0
#         for i in range(2, n):
#             if i in notPrimes: continue
#             res += 1
            
#             for j in range(i * i, n, i):
#                 notPrimes.add(j)
        
#         return res

# Improved
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        
        primes = [1 for i in range(n)]
        primes[0] = primes[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # for j in range(i * i, n, i):
                #     primes[j] = 0
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
        
        return sum(primes)
