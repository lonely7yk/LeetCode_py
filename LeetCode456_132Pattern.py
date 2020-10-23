"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] 
and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 10^4
-10^9 <= nums[i] <= 10^9
"""

from typing import List


# Stack: O(n)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        third = float('-inf')
        stack = []
        
        # 从后往前遍历
        for i in range(n - 1, -1, -1):
            num = nums[i]
            # num < third, 说明第一个数找到了
            if num < third: 
                return True
            else:
                # num > 栈顶元素，说明 num 的后面有比他小的元素，这个时候更新 third 为比 num 小的最大元素
                # second 这个时候就是 num
                while stack and stack[-1] < num:
                    third = stack.pop()
                    
            stack.append(num)
            
        return False
            
        

