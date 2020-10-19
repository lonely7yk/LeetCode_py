"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the 
values in B are the same.

If it cannot be done, return -1.

Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal 
to 2, as indicated by the second figure.

Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Constraints:

2 <= A.length == B.length <= 2 * 10^4
1 <= A[i], B[i] <= 6
"""


from typing import List


# Greedy: O(n)
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        cntMap = collections.defaultdict(lambda: 0)

        # 先找到频率大于等于 n 的数
        sameNum = -1
        for a, b in zip(A, B):
            cntMap[a] += 1
            cntMap[b] += 1
            
            if cntMap[a] >= n: sameNum = a
            if cntMap[b] >= n: sameNum = b
            
        if sameNum == -1: return -1
        swap2ANum = 0
        swap2BNum = 0
        # 根据这个数看切换到 A 数量少还是 B 数量少
        for i in range(n):
            if A[i] != sameNum and B[i] != sameNum: return -1
            
            if A[i] != sameNum:
                swap2ANum += 1
            if B[i] != sameNum:
                swap2BNum += 1
                
        return min(swap2ANum, swap2BNum)
                
