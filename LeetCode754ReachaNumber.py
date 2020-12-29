"""
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n 
steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""


# Math: O(1)
# https://leetcode.com/problems/reach-a-number/solution/
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = 0
        curr = 0
        
        # while curr < target:
        #     step += 1
        #     curr += step
        step = math.ceil(math.sqrt(2 * target + 0.25) - 0.5)
        curr = (step + 1) * step // 2
        
        if curr == target: return step
        
        delta = curr - target
        if delta % 2 == 0:
            return step
        elif (delta + step + 1) % 2 == 0:
            return step + 1
        else:
            return step + 2
        
