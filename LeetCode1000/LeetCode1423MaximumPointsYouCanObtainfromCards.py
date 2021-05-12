"""
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 

Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 
Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""

from typing import List


# # DP: O(n) - O(n)
# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         n = len(cardPoints)
#         left = [0 for i in range(n + 1)]  # 从左到右长度为
#         right = [0 for j in range(n + 1)]
        
#         for i in range(1, n + 1):
#             left[i] = left[i - 1] + cardPoints[i - 1]
#             right[i] = right[i - 1] + cardPoints[n - i]
            
#         res = 0
#         for i in range(k + 1):
#             res = max(res, left[i] + right[k - i])
            
#         return res


# Sliding Window: O(n) - O(1)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        i, j = 0, n - k - 1
        res = 0
        tot = sum(cardPoints)
        curWin = sum(cardPoints[i:j+1])
        
        while True:
            res = max(res, tot - curWin)
            
            i += 1
            j += 1
            
            if j == n: break
            curWin = curWin - cardPoints[i - 1] + cardPoints[j]
            
        return res

