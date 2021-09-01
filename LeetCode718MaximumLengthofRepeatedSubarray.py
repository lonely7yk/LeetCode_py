"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in 
both arrays.

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""

from typing import List


# # DP: O(mn) - O(mn)
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         m, n = len(nums1), len(nums2)
#         dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
#         max_len = 0
        
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 if nums1[i] == nums2[j]:
#                     dp[i][j] = dp[i + 1][j + 1] + 1
#                     max_len = max(max_len, dp[i][j])
                    
#         return max_len


# # DP improve: O(mn) - O(n)
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         m, n = len(nums1), len(nums2)
#         dp = [0 for j in range(n + 1)]
#         max_len = 0
        
#         for i in range(m - 1, -1, -1):
#             for j in range(n):
#                 if nums1[i] == nums2[j]:
#                     dp[j] = dp[j + 1] + 1
#                     max_len = max(max_len, dp[j])
#                 else:
#                     dp[j] = 0
                    
#         return max_len


# # Sliding Window: O((m + n) * min(m, n)) - O(1)
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         n1, n2 = len(nums1), len(nums2)
        
#         def max_length(s1, s2):
#             l1 = n1 - s1
#             l2 = n2 - s2
#             length = min(l1, l2)
#             max_len = 0
#             k = 0
            
#             for i in range(length):
#                 if nums1[s1 + i] == nums2[s2 + i]:
#                     k += 1
#                     max_len = max(max_len, k)
#                 else:
#                     k = 0
                    
#             return max_len
        
#         res = 0
#         for i in range(n1):
#             res = max(res, max_length(i, 0))
            
#         for j in range(n2):
#             res = max(res, max_length(0, j))
            
#         return res


# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/
# 也可参考 LC1004
# Rolling hash + Binary Search: O((m+n)log(min(n1, n2))) - O(n)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10 ** 9 + 9
        n1, n2 = len(nums1), len(nums2)
        
        # 检验长度为 L 的情况下，是否能找到两数组有共同部分
        def helper(L):
            p = (113 ** L) % mod
            cur_hash = functools.reduce(lambda x, y: (113 * x + y) % mod, nums1[:L], 0)
            seen = collections.defaultdict(list)
            seen[cur_hash].append(0)
            
            # 把 nums1 中长度为 L 的子数组都过一遍
            for i in range(L, n1):
                cur_hash = (cur_hash * 113 - p * nums1[i - L] + nums1[i]) % mod
                seen[cur_hash].append(i - L + 1)    # dict 的 value 保存的是所有子数组的第一个索引
            
            cur_hash = functools.reduce(lambda x, y: (113 * x + y) % mod, nums2[:L], 0)
            if cur_hash in seen:
                cur_list = nums2[:L]
                for idx in seen[cur_hash]:
                    tmp_list = nums1[idx:idx+L]
                    if cur_list == tmp_list:
                        return True
            
            for i in range(L, n2):
                cur_hash = (cur_hash * 113 - p * nums2[i - L] + nums2[i]) % mod
                if cur_hash in seen:
                    cur_list = nums2[i-L+1:i+1]
                    for idx in seen[cur_hash]:
                        tmp_list = nums1[idx:idx+L]
                        if cur_list == tmp_list:
                            return True
                        
            return False
        
        left, right = 0, min(n1, n2) + 1
        res = 0
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                left = mid + 1
                res = mid
            else:
                right = mid
                
        return res
