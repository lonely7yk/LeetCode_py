"""
You have a number of envelopes with widths and heights given as a pair of 
integers (w, h). One envelope can fit into another if and only if both the 
width and height of one envelope is greater than the width and height of the 
other envelope.

What is the maximum number of envelopes can you Russian doll? (put one 
inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 

Explanation: The maximum number of envelopes you can Russian doll is 3 
([2,3] => [5,4] => [6,7]).
"""

from typing import List
import functools

class Solution:
    # # DP: O(n^2) TLE
    # # 对 width 进行排序后，用类似 300 题的方法找最长递增子串
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #     if not envelopes: return 0

    #     n = len(envelopes)
    #     envelopes = sorted(envelopes, key=lambda tmp:tmp[0])
    #     dp = [1 for i in range(n)]
    #     res = 1

    #     for i in range(1, n):
    #         envelope = envelopes[i]

    #         for j in range(i):
    #             if envelope[0] > envelopes[j][0] and envelope[1] > envelopes[j][1]:
    #                 dp[i] = max(dp[i], dp[j] + 1)

    #             res = max(res, dp[i])

    #     return res

    # DP: O(nlogn) 172ms 44.44%
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # def mycmp(env1, env2):
        #     # 如果 width 不同，就根据 width 正序排序
        #     # 如果 width 相同，就根据 height 逆序排序
        #     # 这是这道题的关键，因为这样在后续更新 list_ 时，遇到相同的width可以直接更新list_，不用判断width
        #     if env1[0] != env2[0]:
        #         return env1[0] - env2[0]
        #     else:
        #         return env2[1] - env1[1]

        if not envelopes: return 0

        n = len(envelopes)
        # envelopes = sorted(envelopes, key=functools.cmp_to_key(mycmp))
        # envelopes.sort(key=functools.cmp_to_key(mycmp))
        envelopes.sort(key=lambda x:(x[0], -x[1]))  # 用 lambda 排序明显快
        list_ = []

        for envelope in envelopes:
            height = envelope[1]

            if not list_ or height > list_[-1]:
                list_.append(height)
            else:
                left, right = 0, len(list_)
                while left < right:
                    mid = (right - left) // 2 + left
                    if list_[mid] < height:
                        left = mid + 1
                    else:
                        right = mid

                list_[left] = height

        return len(list_)


if __name__ == '__main__':
    # envelopes = [[5,4],[6,4],[6,7],[2,3]]
    envelopes = [[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]

    res = Solution().maxEnvelopes(envelopes)
    print(res)
