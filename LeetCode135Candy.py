"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""

from typing import List

class Solution:
    # # Greedy: O(n): 176ms 63.75%
    # # 参考：https://leetcode.com/problems/candy/discuss/42769/A-simple-solution
    # # 先初始化所有为1，从左往右走一遍，如果当前的比前一个大，就在前一个基础上加 1
    # # 然后从右往左走一遍，如果当前的比后一个大，就在后一个基础上加 1，但是如果当前的比后一个加1更大，说明当前的是从左往右递增的最高点
    # def candy(self, ratings: List[int]) -> int:
    #     n = len(ratings)
    #     candies = [1 for i in range(n)]

    #     for i in range(1, n):
    #         if ratings[i] > ratings[i - 1]:
    #             candies[i] = candies[i - 1] + 1

    #     for i in reversed(range(0, n - 1)):
    #         if ratings[i] > ratings[i + 1]:
    #             candies[i] = max(candies[i + 1] + 1, candies[i])

    #     return sum(candies)

    # Greedy: O(n) 164ms 91.24%
    # 参考：http://www.allenlipeng47.com/blog/index.php/2016/07/21/candy/
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        countDown = 0
        pre = 1
        total = 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                if countDown > 0:
                    total += countDown * (1 + countDown) // 2
                    if countDown >= pre:
                        total += countDown - pre + 1
                    pre = 1
                    countDown = 0
                pre = 1 if ratings[i] == ratings[i - 1] else pre + 1
                total += pre
            else:
                countDown += 1

        if countDown > 0:
            total += countDown * (1 + countDown) // 2
            if countDown >= pre:
                total += countDown - pre + 1

        return total

if __name__ == '__main__':
    # ratings = [1,0,2]
    # ratings = [1,2,2]
    ratings = [1,3,2,2,1]

    res = Solution().candy(ratings)
    print(res)
