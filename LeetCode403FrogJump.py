"""
A frog is crossing a river. The river is divided into x units and at 
each unit there may or may not exist a stone. The frog can jump on a 
stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog is able to cross the river by landing on the last 
stone. Initially, the frog is on the first stone and assume the first 
jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be 
either k - 1, k, or k + 1 units. Note that the frog can only jump 
in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.

Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
"""

from typing import List
import functools

# class Solution:
    # # DP+HashSet: O(n^2) 2616ms 5%
    # def canCross(self, stones: List[int]) -> bool:
    #     if len(stones) <= 1: return True
    #     if stones[1] != 1: return False
        
    #     n = len(stones)
    #     dp = [set() for i in range(n)]  # 表示第 i 块石头上可以跳多少步的集合
    #     dp[1].add(1)
        
    #     for i in range(2, n):
    #         for j in range(i - 1, 0, -1):
    #             gap = stones[i] - stones[j]
    #             if gap - 1 in dp[j] or gap + 1 in dp[j] or gap in dp[j]:
    #                 dp[i].add(gap)
        
    #     return dp[n - 1]

    # # HashMap+HashSet: 216ms  60%
    # def canCross(self, stones: List[int]) -> bool:
    #     if len(stones) <= 1: return True
    #     if stones[1] != 1: return False
        
    #     n = len(stones)
    #     dp = {}
    #     for stone in stones:
    #         dp[stone] = set()
    #     dp[0].add(1)

    #     for i in range(n):
    #         stone = stones[i]
    #         for step in dp[stone]:
    #             if step + stone == stones[-1]: return True
                
    #             if step + stone in dp:
    #                 if step - 1 > 0: dp[step + stone].add(step - 1)
    #                 dp[step + stone].add(step)
    #                 dp[step + stone].add(step + 1)
                    
    #     return False


# DFS + memo
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @functools.lru_cache(None)
        def dfs(pos, lastStep, target):
            if pos == target: return True
            if pos > target: return False
            if pos not in stoneSet: return False
            
            res = False
            res = dfs(pos + lastStep, lastStep, target) | dfs(pos + lastStep + 1, lastStep + 1, target)
            if lastStep > 1:
                res |= dfs(pos + lastStep - 1, lastStep - 1, target)
                
            return res
        
        if stones[1] != 1: return False
        stoneSet = set(stones)
        return dfs(1, 1, stones[-1])

        
                    
if __name__ == '__main__':
    stones = [0,1,3,4,5,7,9,10,12]

    res = Solution().canCross(stones)
    print(res)