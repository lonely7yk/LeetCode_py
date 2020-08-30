"""
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
"""

from typing import List
import collections


# Union Find: 先算每个数的 prime factors，然后把每个 factor 中的所有数都 union 起来
# 最后计算每个 union 有多少个数
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def find(roots, x):
            if x == roots[x]:
                return x
            else:
                roots[x] = find(roots, roots[x])
                return roots[x]

        # 找到 num 的所有 prime 的 factors
        def primeSet(num):
            primes = []
            factor = 2

            while num >= factor * factor:
                if num % factor == 0:
                    primes.append(factor)
                    num //= factor
                else:
                    factor += 1

            primes.append(num)
            return set(primes)

        n = len(A)
        roots = list(range(n))
        size = [1 for i in range(n)]    # 存储每个根节点下面的子节点个数
        factorMap = collections.defaultdict(list)

        # 对每一个数，找到所有 prime factors，并存在一个 map 中
        for i, a in enumerate(A):
            primes = primeSet(a)
            for prime in primes:
                factorMap[prime].append(i)

        res = 1
        for factor, idxList in factorMap.items():
            for i in range(len(idxList) - 1):
                root1 = find(roots, idxList[i])
                root2 = find(roots, idxList[i + 1])

                # 这里尝试过 union by rank 发现效果不如直接 union 好
                if root1 != root2:
                    roots[root2] = root1
                    size[root1] += size[root2]
                    res = max(res, size[root1])

        return res