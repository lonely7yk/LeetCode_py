from typing import List
import heapq

# # Greedy: O(n) 56ms 41%
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         max1 = float('-inf')
#         max2 = float('-inf')
#         max3 = float('-inf')

#         for n in nums:
#             if n in (max1, max2, max3): continue    # 如果数字已经存在，直接跳过

#             if n > max1:
#                 max1, max2, max3 = n, max1, max2
#             elif n > max2:
#                 max2, max3 = n, max2
#             elif n > max3:
#                 max3 = n

#         return max3 if max3 != float('-inf') else max1

# heap + set: O(n) 52ms 72%
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        set_ = set()

        for num in nums:
            if num in set_: continue

            heapq.heappush(heap, num)
            set_.add(num)

            # 把堆的大小保持在 3
            if len(heap) > 3:
                heapq.heappop(heap)

        if len(heap) == 3:
            return heap[0]
        else:
            return max(nums)


nums = [1,1,2]
res = Solution().thirdMax(nums)
print(res)
