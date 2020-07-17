"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements 
is unique.
You can return the answer in any order.
"""

import collections
from typing import List
import heapq

# bucket sort: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntMap = collections.defaultdict(lambda : 0)
        buckets = [None for i in range(len(nums) + 1)]

        # 统计每个数的频率
        for num in nums:
            cntMap[num] += 1

        # 每个桶里存放对应频率的 num
        for num,cnt in cntMap.items():
            if buckets[cnt] is None: buckets[cnt] = []
            buckets[cnt].append(num)

        res = []
        for bucket in reversed(buckets):
            if len(res) >= k: break
            if bucket is None: continue
            res.extend(bucket)

        return res

# # heap: O(nlogk)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         cntMap = collections.defaultdict(lambda : 0)
#         heap = []

#         for num in nums:
#             cntMap[num] += 1

#         for num,cnt in cntMap.items():
#             heapq.heappush(heap, (cnt, num))
#             if len(heap) > k: heapq.heappop(heap)

#         return [x for _,x in heap]


# # QuickSearch: O(nlogn)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         def partition(unique, counter, left, right):
#             pivot = counter[unique[left]]
#             i, j = left, right
            
#             while i < j:
#                 while i < j and pivot >= counter[unique[j]]: j -= 1
#                 while i < j and counter[unique[i]] >= pivot: i += 1
                    
#                 if i < j:
#                     unique[i], unique[j] = unique[j], unique[i]
#                 else:
#                     unique[left], unique[j] = unique[j], unique[left]
            
#             return j
        
#         def quickSearch(unique, counter, left, right):
#             mid = partition(unique, counter, left, right)
#             if mid == k - 1: return
#             elif mid > k - 1: quickSearch(unique, counter, left, mid - 1)
#             else: quickSearch(unique, counter, mid + 1, right)
        
#         counter = Counter(nums)
#         unique = list(counter.keys())
#         quickSearch(unique, counter, 0, len(unique) - 1)
#         return unique[:k]

nums = [1,1,1,2,2,3]
k = 2

# nums = [1]
# k = 1
res = Solution().topKFrequent(nums, k)
print(res)



