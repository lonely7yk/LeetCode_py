"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

from typing import List

class Solution:
    # 法一： O(n)-O(1) 36ms 74.8%
    # 参考：https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c%2B%2B-solution-O(1)-space-and-O(n)-time
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 1
        
        def swap(x, y):
            tmp = nums[x]
            nums[x] = nums[y]
            nums[y] = tmp

        for i in range(len(nums)):
            # 这句 while 是关键，要一直换到不能换为止，直到交换的两个数一样
            while 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                swap(i, nums[i] - 1)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

    # # 法二：O(n)-O(1) 36ms 74.8%
    # # 参考：https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
    # # l 为长度，则可能的结果为 [1,2,...,l+1]，把不可能的去掉。然后对剩下的值，做 l+1 取模的索引加上 l+1
    # # 最后如果值存在，则在对应索引的值一定大于 l+1
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     if not nums or len(nums) == 0: return 1

    #     l = len(nums)
    #     # 使 nums 的长度增长 1，使之长度变为 l+1
    #     nums.append(0)

    #     for i in range(l + 1):
    #         if nums[i] < 0 or nums[i] >= l + 1:
    #             nums[i] = 0

    #     for i in range(l + 1):
    #         nums[nums[i] % (l + 1)] += (l + 1)

    #     for i in range(1, l + 1):
    #         if nums[i] // (l + 1) == 0:
    #             return i

    #     return l + 1

    # # 法三：O(n)-O(1)
    # # 先判断 1 是否存在与 nums 中，如果不在直接返回 1. 否则，把所有不在 (1, n+1) 范围的数都改成 1。
    # # 遍历一遍数组，把 nums[i] 看成索引，把对应索引位置设置为负数。
    # # 最后看索引 2~n+1 索引位置的数为正数的第一个索引，就是第一个没出现的数
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     flag1 = False   # 1 是否存在于 nums 中
    #     for i in range(n):
    #         if nums[i] == 1:
    #             flag1 = True
                
    #         if nums[i] <= 0 or nums[i] > n + 1:
    #             nums[i] = 1
                
    #     if not flag1: return 1
        
    #     # 是 nums 长度变为 n+2 这样就会有 2~n+1 的索引
    #     # 如果不想修改 nums 长度，可以把 0 索引用来存储第 n 个数
    #     nums.append(1)
    #     nums.append(1)
        
    #     for i in range(n + 2):
    #         idx = abs(nums[i])
    #         if nums[idx] > 0:
    #             # 出现过的数标记成负数
    #             nums[idx] = -nums[idx]
        
    #     for i in range(2, n + 2):
    #         if nums[i] > 0:
    #             return i
            
    #     return -1

if __name__ == '__main__':
    # nums = [1,2,0]
    # nums = [3,4,-1,1]
    nums = [2,2]
    res = Solution().firstMissingPositive(nums)
    print(res)
