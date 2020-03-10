"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

from typing import List

# 从某个当前最高高度 currMax 开始往后，只要在后面存在比 currMax 大的高度，那之间的高度都可以使用 currMax-height[i] 来计算
# 所以不妨先找到最高高度的索引，然后从两边往中间进行计算，这样在最后就一样有一个高度高于前一个高度
# # Greedy: O(n) O(1) 36ms 99.8%
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height: return 0

#         maxH = 0
#         maxIdx = 0
#         n = len(height)

#         # 找到最高的位置
#         for i in range(n):
#             if height[i] > maxH:
#                 maxH = height[i]
#                 maxIdx = i

#         currMax = 0 # 表示当前最高高度
#         res = 0

#         # 如果高度大于当前高度，则更新当前最高高度，否则直接加上 (currMax - h)
#         # 因为在该高度后面一定有一块板比 currMax 大（height[maxIdx]）
#         for i in range(maxIdx + 1):
#             h = height[i]
#             if h >= currMax: currMax = h
#             else: res += (currMax - h)

#         currMax = 0

#         # 正着做一次，反着做一次就出结果了
#         for i in range(n - 1, maxIdx - 1, -1):
#             h = height[i]
#             if h >= currMax: currMax = h
#             else: res += (currMax - h)

#         return res

# # left 表示从左到右到 i 为止的最大值，right 表示从右到左到 i 为止的最大值
# # 那么对于每一个高度所能积累的水量就是 min(left[i], right[i]) - height[i]
# # DP: O(n) O(n) 52ms 66%
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height: return 0

#         n = len(height)
#         left = [0 for i in range(n)]    # 表示从左到右到 i 为止的最大值
#         right = [0 for i in range(n)]   # 表示从右到左到 i 为止的最大值
#         leftMax = 0
#         rightMax = 0
#         res = 0

#         for i in range(n):
#             left[i] = leftMax = max(leftMax, height[i])
#             right[n - i - 1] = rightMax = max(rightMax, height[n - i - 1])

#         for i in range(n):
#             res += min(left[i], right[i]) - height[i]

#         return res


# 两个指针指向数组的两头，每次都比较左右两头指针位置对应的 leftMax 和 rightMax
# 如果 leftMax < rightMax，说明 leftMax 是 bottleneck，直接用 leftMax - height[left]
# 并更新 left 和 leftMax。反之亦然。
# Two pointers: O(n) O(1) 44ms 95.6%
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)
        left, right = 0, n - 1
        leftMax, rightMax = height[0], height[-1]
        res = 0

        while left <= right:
            if leftMax < rightMax:
                res += (leftMax - height[left])
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                res += (rightMax - height[right])
                right -= 1
                rightMax = max(rightMax, height[right])

        return res



height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = Solution().trap(height)
print(res)
