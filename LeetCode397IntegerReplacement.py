'''
Given a positive integer n and you can do operations as follow:

1. If n is even, replace n with n/2.
2. If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
'''

from collections import deque


class Solution:
    # # DP: TLE
    # def integerReplacement(self, n: int) -> int:
    #     if n == 1: return 0

    #     dp = [0 for i in range(n + 1)]
    #     dp[2] = 1

    #     for i in range(3, n + 1):
    #         if i % 2 == 0:
    #             dp[i] = dp[int(i / 2)] + 1
    #         else:
    #             dp[i] = min(dp[int((i + 1) / 2)], dp[int((i - 1) / 2)]) + 2

    #     return dp[n]

    # # BFS: O(logn) 28ms 91%
    # def integerReplacement(self, n: int) -> int:
    #     queue = deque()
    #     set_ = set()    # 表示已经添加过的节点
    #     queue.append(n)
    #     set_.add(n)
    #     cnt = 0

    #     while len(queue) != 0:
    #         n = len(queue)
    #         for i in range(n):
    #             first = queue.popleft()
    #             if first == 1: return cnt
    #             if first % 2 == 0:
    #                 tmp = first // 2
    #                 # 如果结点已经添加过就不需要重复添加，因此这次添加的结果一定大于等于上次添加的结果
    #                 if tmp not in set_:
    #                     queue.append(tmp)
    #                     set_.add(tmp)
    #             else:
    #                 if first + 1 not in set_:
    #                     queue.append(first + 1)
    #                     set_.add(first + 1)
    #                 if first - 1 not in set_:
    #                     queue.append(first - 1)
    #                     set_.add(first - 1)
    #         cnt = cnt + 1

    #     return 0

    # Math Method: O(logn) 28ms 91%
    # 参考：https://blog.csdn.net/fuxuemingzhu/article/details/79495908
    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n != 1:
            # 如果除以4余数时3且本身不是3则加1，如果除以4余数时1或本身是3则减1，否则除2
            if n % 4 == 3 and n != 3:
                n = n + 1
            elif n % 4 == 1 or n == 3:
                n = n - 1
            else:
                n = n // 2
            cnt += 1
        return cnt

if __name__ == '__main__':
    solution = Solution()
    print(solution.integerReplacement(8))