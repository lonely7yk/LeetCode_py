"""
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you
currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow
ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the
value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you
initially own. You are also given an integer orders, which represents the total number of balls that the customer wants.
You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large,
return it modulo 109 + 7.

Example 1:

Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.

Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.

Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.


Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)
"""

from typing import List
import collections


# # O(nlogn)
# class Solution:
#     def maxProfit(self, inventory: List[int], orders: int) -> int:
#         counter = collections.Counter(inventory)
#         cntList = sorted(list(counter.items()))
#         cntList = [(0, 0)] + cntList
#         res = 0
#
#         while orders:
#             k1, v1 = cntList.pop()
#             k2, v2 = cntList.pop()
#
#             if (k1 - k2) * v1 <= orders:
#                 res += (k1 + k2 + 1) * (k1 - k2) // 2 * v1
#                 orders -= (k1 - k2) * v1
#
#                 v2 += v1
#                 cntList.append((k2, v2))
#             else:
#                 num = orders // v1
#                 res += (k1 - num + 1 + k1) * num // 2 * v1 + (k1 - num) * (orders % v1)
#                 orders = 0
#
#         return res % (10 ** 9 + 7)


# Binary Search: O(nlogn)
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # 判断所有高于 mid 的球都降到 mid 是否能满足 orders
        def judge(mid, orders):
            cnt = 0
            for k,v in cntList:
                if k < mid: break
                cnt += (k - mid) * v
                if cnt > orders: return True
            return cnt > orders

        counter = collections.Counter(inventory)
        cntList = sorted(counter.items(), reverse=True)

        left = 0
        right = cntList[0][0]

        # 二分搜索结束后，降到 left-1 是能包含所有 orders 的最大值
        while left < right:
            mid = (left + right) // 2
            # 不能满足，说明 mid 太小了
            if judge(mid, orders):
                left = mid + 1
            else:
                right = mid

        # 把所有能降到 left 的 orders 都加到 res 中
        res = 0
        for k,v in cntList:
            if k < left: break
            res += (left + 1 + k) * (k - left) // 2 * v
            orders -= v * (k - left)

        # 把剩下降到 left-1
        res += orders * left
        return res % (10 ** 9 + 7)


inventory = [2,5]
orders = 4
res = Solution().maxProfit(inventory, orders)
print(res)
