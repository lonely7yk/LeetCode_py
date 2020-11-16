"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""

from typing import List


# Greedy: O(n)
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        i = 1
        
        # 找到第一个上升的位置 A[i - 1] < A[i]
        while i < n and A[i - 1] >= A[i]:
            i += 1
            
        inc = True  # 表示现在的状态是升序还是降序
        maxLen = 0  # 最大 mountain 的长度
        start = i - 1
        
        while i < n:
            if A[i] > A[i - 1]:
                # 如果在降序状态遇到升序，就改变 start
                if not inc:
                    start = i - 1
                    inc = True
                i += 1
            elif A[i] < A[i - 1]:
                # 如果遇到降序状态，改变 inc，并更新 maxLen
                inc = False
                maxLen = max(maxLen, i - start + 1)
                i += 1
            else:
                # 如果相等，一直找到第一个上升的位置
                while i < n and A[i - 1] >= A[i]:
                    i += 1
                start = i - 1
                
        return maxLen 
