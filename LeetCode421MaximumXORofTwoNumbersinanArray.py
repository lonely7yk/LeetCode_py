"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

from typing import List


# Bit Manipulation: O(n)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxValue = 0    # 当前可以达到的最大结果
        mask = 0

        for i in range(31, -1, -1):
            # 用于取前缀
            mask = mask | 1 << i
            prefixes = set()

            # 得到所有数的前缀，放到 prefixes 中
            for num in nums:
                prefixes.add(num & mask)

            greedyTry = maxValue | 1 << i
            # 确定 prefixes 是否有两个 prefix 的异或结果为 greedyTry，如果是则说明 maxValue 目前可以到达 greedyTry
            for prefix in prefixes:
                # 注意这里，因为有一个公式  a^b=c <==> a^c=b，所以 anotherPrefix 可以用 prefix ^ greedyTry 求出来
                anotherPrefix = prefix ^ greedyTry
                if anotherPrefix in prefixes:
                    maxValue = greedyTry
                    break

        return maxValue


# # Trie
# class TrieNode:
#     def __init__(self):
#         self.children = [None, None]

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def addNode(self, num):
#         p = self.root
#         for i in range(31, -1, -1):
#             curBit = (num >> i) & 1
#             if not p.children[curBit]:
#                 p.children[curBit] = TrieNode()
#             p = p.children[curBit]

# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         trie = Trie()
#         res = 0

#         # Build Trie
#         for num in nums:
#             trie.addNode(num)

#         for num in nums:
#             p = trie.root
#             curVal = 0

#             for i in range(31, -1, -1):
#                 curBit = (num >> i) & 1
#                 # 如果是 0，就看 1 是否存在 children 中，如果是 1 就看 0 是否存在 children 中
#                 if p.children[curBit ^ 1]:
#                     curVal = curVal | (1 << i)
#                     p = p.children[curBit ^ 1]
#                 else:
#                     p = p.children[curBit]

#             res = max(res, curVal)

#         return res


nums = [3, 10, 5, 25, 2, 8]
res = Solution().findMaximumXOR(nums)
print(res)
