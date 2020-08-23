"""
Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that
initially has all its bits set to zero.

At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set
to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m.
A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

Example 1:

Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.

Example 2:

Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.

Example 3:

Input: arr = [1], m = 1
Output: 1

Example 4:

Input: arr = [2,1], m = 2
Output: 2

Constraints:

n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= n
All integers in arr are distinct.
1 <= m <= arr.length
"""

from typing import List
import collections

# # Union Find: O(n log k)  15%
# # 老实说这个方法有点蠢
# class Solution:
#     def findLatestStep(self, arr: List[int], m: int) -> int:
#         def find(roots, x):
#             if x == roots[x]:
#                 return x
#             else:
#                 roots[x] = find(roots, roots[x])
#                 return roots[x]
#
#         n = len(arr)
#         roots = [-1 for i in range(n + 1)]  # 保存父节点索引
#         size = [0 for i in range(n + 1)]    # 树大小
#         res = -1
#         rootSet = set()     # 根节点的 set
#         maxSize = 1         # 当前所有根的最大 size
#
#         for i, x in enumerate(arr):
#             roots[x] = x
#             rootSet.add(x)
#             size[x] = 1
#
#             for nxtX in (x - 1, x + 1):
#                 if 1 <= nxtX <= n and roots[nxtX] >= 0:
#                     root1 = find(roots, nxtX)
#                     root2 = find(roots, x)
#
#                     if size[root1] > size[root2]:
#                         roots[root2] = root1
#                         size[root1] += size[root2]
#                         # 因为 root2 合并到 root1 了，把 root2 从 rootSet 中删除
#                         rootSet.remove(root2)
#                         maxSize = max(maxSize, size[root1])
#                     else:
#                         roots[root1] = root2
#                         size[root2] += size[root1]
#                         # 因为 root1 合并到 root2 了，把 root1 从 rootSet 中删除
#                         rootSet.remove(root1)
#                         maxSize = max(maxSize, size[root2])
#
#             # maxSize 小于 m，不进行比较
#             if maxSize < m: continue
#
#             for root in rootSet:
#                 if size[root] == m:
#                     res = i + 1
#
#         return res


# # HashMap: O(n)  37%
# # 和 LC128 差不多的思路，但是只比上面的快了一点点
# class Solution:
#     def findLatestStep(self, arr: List[int], m: int) -> int:
#         res = -1
#
#         # pos: length
#         lenMap = dict()
#         # length: cnt
#         cntMap = collections.defaultdict(lambda: 0)
#
#         for i, x in enumerate(arr):
#             left = 0
#             right = 0
#
#             if x - 1 in lenMap:
#                 left = lenMap[x - 1]
#                 cntMap[left] -= 1
#             if x + 1 in lenMap:
#                 right = lenMap[x + 1]
#                 cntMap[right] -= 1
#
#             newLen = 1 + left + right
#             # 要把 x-left 和 x+right 都改了（边界情况）
#             lenMap[x] = lenMap[x - left] = lenMap[x + right] = newLen
#             cntMap[newLen] += 1
#
#             # 每次必须要保证 m 长度的数量不为 0
#             if cntMap[m] != 0:
#                 res = i + 1
#
#         return res

# HashMap improved: O(n) 50%
# 用数组来替代 map
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1

        n = len(arr)
        # pos: length
        # n + 2 长度是为了让 lenMap[0] 和 lenMap[n + 1] 有值，这样下面 cntMap[left] cntMap[right] 都可以取到
        lenMap = [0 for i in range(n + 2)]
        # length: cnt
        cntMap = [0 for i in range(n + 1)]

        for i, x in enumerate(arr):
            left = lenMap[x - 1]
            right = lenMap[x + 1]

            cntMap[left] -= 1
            cntMap[right] -= 1
            lenMap[x] = lenMap[x - left] = lenMap[x + right] = 1 + left + right
            cntMap[lenMap[x]] += 1

            if cntMap[m]:
                res = i + 1

        return res