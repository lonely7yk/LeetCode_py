"""
Given an array nums, there is a sliding window of size k which is moving from the very left 
of the array to the very right. You can only see the k numbers in the window. Each time the 
sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

from typing import List
import collections

# Deque 单调栈: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = collections.deque()
        res = []
        
        for i, num in enumerate(nums):
            if dq and dq[0] == i - k: dq.popleft()
            while dq and nums[dq[-1]] < num: dq.pop()
            dq.append(i)
            
            if i - k + 1 >= 0: res.append(nums[dq[0]])
            
        return res
        
