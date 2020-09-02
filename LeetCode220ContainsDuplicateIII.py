"""
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute 
difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""

from typing import List

# Bucket Sort: O(n)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0: return False
        
        # nums 中的最大最小值
        minNum = min(nums)
        maxNum = min(nums)
        
        bucket = dict()
        bucketLen = t + 1   # 桶长（保证桶中任意两元素差绝对值小于等于 t）
        
        for i, num in enumerate(nums):
            # 计算在哪个桶
            m = (num - minNum) // bucketLen
            # 已经在桶里，直接返回 True
            if m in bucket: return True
            # 在 m - 1 的桶里，判断两数的差
            if m - 1 in bucket and num - bucket[m - 1] <= t: return True
            # 在 m + 1 的桶里，判断两数的差
            if m + 1 in bucket and bucket[m + 1] - num <= t: return True
            
            bucket[m] = num
            # 保证桶的个数为 k + 1，这样任意两数的索引差小于等于 k
            if i >= k: bucket.pop((nums[i - k] - minNum) // bucketLen)
                
        return False
        