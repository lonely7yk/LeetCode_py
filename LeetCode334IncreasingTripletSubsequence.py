"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such 
that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

from typing import List


# # LIS: O(N log3)
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         l = []
        
#         for num in nums:
#             if not l or num > l[-1]:
#                 l.append(num)
#                 if len(l) == 3: return True
#             else:
#                 idx = bisect.bisect_left(l, num)
#                 l[idx] = num
        
#         return False



# Linear Scan: O(N)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
            
        return False

