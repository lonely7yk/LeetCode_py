"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most 
twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array 
in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer, but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input 
array will be known to the caller.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums 
being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3]
Explanation: Your function should return length = 7, with the first seven elements of nums being 
modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It doesn't matter what values are set beyond 
the returned length.
 
Constraints:

0 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in ascending order.
"""

from typing import List


# O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        
        idx1 = 1
        idx2 = 1
        lastVal = nums[0]
        cnt = 1
        
        while idx2 < len(nums):
            if nums[idx2] == nums[idx2 - 1]:
                cnt += 1
            else:
                lastVal = nums[idx2]
                cnt = 1
                
            if cnt <= 2:
                nums[idx1] = nums[idx2]
                idx1 += 1
                
            idx2 += 1
            
        return idx1
        
