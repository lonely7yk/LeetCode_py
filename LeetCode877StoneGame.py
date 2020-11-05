"""
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, 
and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so 
there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of 
stones from either the beginning or the end of the row.  This continues until there are no more 
piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

from typing import List


# # DP: O(n^2)
# # dp[i+1][j+1] 表示 piles[i] ... piles[j] 中 Alex 能取得的最大分数
# # 用 dp[i+1][j+1] 而不用 dp[i][j] 是为了防止边界越界
# # 如果 i~j 长度为偶数，说明这次 Alex 取，返回 max(piles[i] + dp[i + 2][j + 1], piles[j] + dp[i + 1][j])
# # 如果为奇数，说明这次 Lee 取，返回 min(-piles[i] + dp[i + 2][j + 1], -piles[j] + dp[i + 1][j])
# # 最后如果 dp[1][n] > 0 说明 Alex 能获胜
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         n = len(piles)
#         dp = [[0 for j in range(n + 2)] for i in range(n + 2)]
        
#         for l in range(1, n + 1):
#             for i in range(n - l + 1):
#                 j = i + l - 1
#                 if l % 2 == 0:
#                     dp[i + 1][j + 1] = max(piles[i] + dp[i + 2][j + 1], piles[j] + dp[i + 1][j])
#                 else:
#                     dp[i + 1][j + 1] = min(-piles[i] + dp[i + 2][j + 1], -piles[j] + dp[i + 1][j])
                    
#         return dp[1][n] > 0


# Math: O(1)
# 如果只有两堆，那 Alex 一定能赢
# 如果有四堆，Alex 也同样能赢，如果 Alex 第一次取第一堆，那 Alex 一定能在第二次取第三堆
# 如果 Alex 第一次取第四堆，那 Alex 一定能在第二次取第二堆。第一堆+第三堆 和 第二堆+第四堆一定是能分胜负的，所以 Alex 一定能赢
# 同理，对于有 n 堆，我们可以把 1，3，5，7... 和 2，4，6，8... 分成两份。Alex 一定能取到其中一份的所有堆，所以 Alex 一定能赢
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:        
        return True
        
