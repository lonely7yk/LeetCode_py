"""
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move 
is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.

Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  
So the task is impossible.

Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 

Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""

# 3D DP: O(n^3/k) - O(kn^2)
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        inf = float('inf')
        
        if n == 1: return 0
        if (n - K) % (K - 1) != 0: return -1
        
        preSum = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
        
        @functools.lru_cache(None)
        def dfs(i, j, m):
            if i == j: return 0 if m == 1 else inf
            if (j - i + 1 - m) % (K - 1): return inf
            if m == 1: return dfs(i, j, K) + preSum[j + 1] - preSum[i]

            res = inf
            for mid in range(i, j):
                res = min(res, dfs(i, mid, 1) + dfs(mid + 1, j, m - 1))
            return res
            
        res = dfs(0, n - 1, 1)
        return res if res != inf else -1
        
