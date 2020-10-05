"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it 
does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""

from typing import List


# # Brute force: O(mn)
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         idxMap = dict()
#         res = []
        
#         for idx, num in enumerate(nums2):
#             idxMap[num] = idx
            
#         for num in nums1:
#             idx = idxMap[num]
#             cur = -1
#             for i in range(idx + 1, len(nums2)):
#                 if nums2[i] > num:
#                     cur = nums2[i]
#                     break
                    
#             res.append(cur)
            
#         return res
                
        
# Stack: O(m + n)
# https://leetcode.com/problems/next-greater-element-i/solution/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greaterDict = dict()
        
        for num in nums2:
            while stack and num > stack[-1]:
                greaterDict[stack.pop()] = num
                
            stack.append(num)
            
        while stack:
            greaterDict[stack.pop()] = -1
            
        return [greaterDict[num] for num in nums1]
