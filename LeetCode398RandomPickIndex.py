'''
Given an array of integers with possible duplicates, randomly output 
the index of a given target number. You can assume that the given 
target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra 
space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index 
// should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
'''

import random

# # dict: 348ms 54%
# class Solution:

#     def __init__(self, nums: List[int]):
#         self.idxDict = dict()

#         for i in range(len(nums)):
#             num = nums[i]
#             if num not in self.idxDict:
#                 self.idxDict[num] = [i]
#             else:
#                 self.idxDict[num].append(i)

#     def pick(self, target: int) -> int:
#         idxList = self.idxDict[target]
#         return idxList[random.randint(0, len(idxList) - 1)]

# reservoir sample: 316ms 87.4% 
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = 0
        res = -1
        for idx, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if random.randint(1, cnt) == cnt:
                    res = idx
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

if __name__ == '__main__':
    d = dict()
    
