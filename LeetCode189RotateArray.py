"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""

# # has extra space
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
        
#         idx = n - k
#         nums[:] = nums[n-k:] + nums[:n-k]
        

# # cyclic replacement: O(n) O(1)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n
#         start = 0
#         cnt = 0
        
#         while cnt < n:
#             # 从 start 开始，每隔 k 换一次
#             curIdx, preVal = start, nums[start]
#             while True:
#                 nxtIdx = (curIdx + k) % n
#                 nums[nxtIdx], preVal = preVal, nums[nxtIdx]
#                 curIdx = nxtIdx
#                 cnt += 1
                
#                 if curIdx == start: break
                    
#             start += 1

# reverse: O(n) O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        n = len(nums)
        k %= n
        # 先把所有的 reverse
        reverse(nums, 0, n - 1)
        # 然后把前 k 个 reverse
        reverse(nums, 0, k - 1)
        # 然后把后 n-k 个 reverse
        reverse(nums, k, n - 1)
        