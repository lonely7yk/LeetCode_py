"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:

Input: nums = [4,2,3,4]
Output: 4
 
Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""

from typing import List
import bisect


# # Binary Search: O(n^2logn)
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         # find the index of the last number that is smaller than val from nums[start] to nums[end]
#         def bisect(start, end, val):
#             left, right = start, end
#             while left < right:
#                 mid = (left + right) // 2
#                 if nums[mid] < val:
#                     left = mid + 1
#                 else:
#                     right = mid
            
#             return left - 1
            

#         res = 0
#         n = len(nums)
#         nums.sort()
#         for i in range(n - 2):
#             if nums[i] == 0: continue
#             for j in range(i + 1, n - 1):
#                 if nums[i] + nums[j] <= nums[n - 1]:
#                     idx = bisect(j + 1, n - 1, nums[i] + nums[j])
#                     res += idx - j
#                 else:
#                     res += (1 + n - 1 - j) * (n - 1 - j) // 2
#                     break
                    
#         return res


# # Binary Search (builtin bisect): O(n^2logn)    43%
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         res = 0
#         n = len(nums)
#         nums.sort()
#         for i in range(n - 2):
#             if nums[i] == 0: continue
#             for j in range(i + 1, n - 1):
#                 if nums[i] + nums[j] <= nums[n - 1]:
#                     idx = bisect.bisect_left(nums, nums[i] + nums[j], j + 1, n - 1) - 1
#                     res += idx - j
#                 else:
#                     res += (1 + n - 1 - j) * (n - 1 - j) // 2
#                     break
                    
#         return res


# # Linear Scan: O(n^2) 40%
# # Loop of k and j will be executed O(n^2) times in total, because, we do not reinitialize the value of k for a new value of j.
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         res = 0
#         n = len(nums)
#         nums.sort()
#         for i in range(n - 2):
#             if nums[i] == 0: continue
#             k = i + 2
#             for j in range(i + 1, n - 1):
#                 while k < n and nums[i] + nums[j] > nums[k]: k += 1
#                 res += k - j - 1
                
#         return res


# Two pointer: O(n^2)   60%
class Solution:
    def triangleNumber(self, nums):
        c = 0
        n = len(nums)
        nums.sort()
        for i in range(n-1,1,-1):
            lo = 0
            hi = i - 1
            while lo < hi:
                if nums[hi]+nums[lo] > nums[i]:
                    c += hi-lo
                    hi -= 1
                else:
                    lo += 1
        return c
        

        