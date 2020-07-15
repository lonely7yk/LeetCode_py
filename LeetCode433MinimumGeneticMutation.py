"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
"""

import collections
from typing import List

# DFS: 81%
# class Solution:
#     def minMutation(self, start: str, end: str, bank: List[str]) -> int:
#         # 计算两个字符串中不同字符的个数
#         def diffNum(s1, s2):
#             cnt = 0
#             for c1, c2 in zip(s1, s2):
#                 if c1 != c2: cnt += 1
#             return cnt
        
#         """
#         @params
#         curr: 当前的 genen
#         bank: 剩下的 genens
#         target: 目标的 genen
#         @return
#         从 curr 到 target 需要多少次 mutations
#         """
#         def dfs(curr, bank, target):
#             if curr == target: return 0
#             if not bank: return float('inf')
            
#             res = float('inf')
#             for idx, gene in enumerate(bank):
#                 if diffNum(curr, gene) == 1:
#                     # 新建一个 bank，去掉当前的 gene
#                     tmp = list(bank)
#                     tmp.pop(idx)
#                     res = min(res, 1 + dfs(gene, tmp, target))
                    
#             return res
        
#         res = dfs(start, bank, end)
#         return res if res != float('inf') else -1

# BFS: 11%
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 计算两个字符串中不同字符的个数
        def diffNum(s1, s2):
            cnt = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2: cnt += 1
            return cnt

        queue = collections.deque([start])
        visited = {start}

        # 每一层就多一步
        numStep = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr == end: return numStep

                for nxt in bank:
                    # nxt 没被访问过，且和 curr 距离为 1
                    if nxt not in visited and diffNum(curr, nxt) == 1:
                        visited.add(nxt)
                        queue.append(nxt)

            numStep += 1

        return -1

