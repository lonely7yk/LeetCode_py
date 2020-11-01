"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two 
sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 10^6
"""


# # Binary Search: O(log(m+n))
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)
        
#         m, n = len(nums1), len(nums2)
#         left, right = 0, m
#         totLen = (m + n + 1) // 2
        
#         while left < right:
#             m1 = (left + right) // 2
#             m2 = totLen - m1
            
#             if nums1[m1] < nums2[m2 - 1]:
#                 left = m1 + 1
#             else:
#                 right = m1
                
#         m1 = left
#         m2 = totLen - left
#         maxLeft = max(nums1[m1 - 1] if m1 else float('-inf'), nums2[m2 - 1] if m2 else float('-inf'))
#         minRight = min(nums1[m1] if m1 < m else float('inf'), nums2[m2] if m2 < n else float('inf'))
        
#         if (m + n) % 2 == 0:
#             return (maxLeft + minRight) / 2
#         else:
#             return maxLeft

# Binary Search 另一种写法
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        totLen = (m + n + 1) // 2
        
        while left <= right:
            m1 = (left + right) // 2
            m2 = totLen - m1
            
            if m1 < m and nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            elif m1 > 0 and nums1[m1 - 1] > nums2[m2]:
                right = m1 - 1
            else:
                if m1 == 0: maxLeft = nums2[m2 - 1]
                elif m2 == 0: maxLeft = nums1[m1 - 1]
                else: maxLeft = max(nums1[m1 - 1], nums2[m2 - 1])
                    
                if (m + n) % 2 == 1: return maxLeft
                
                if m1 == m: minRight = nums2[m2]
                elif m2 == n: minRight = nums1[m1]
                else: minRight = min(nums1[m1], nums2[m2])
                    
                return (maxLeft + minRight) / 2
                
        return 0        
        

