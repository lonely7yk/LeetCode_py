"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

from typing import List

# Topo sort
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        beforeCnt = dict()                      # 对于每个字母，排在他前面的有几个
        afterSet = collections.defaultdict(set) # 对于每个字母，他后面的字母的集合
        n = len(words)
        
        # 初始化，所有字母都没有字母排在他前面
        for word in words:
            for c in word:
                beforeCnt[c] = 0
        
        for i in range(n - 1):
            cur = words[i]
            nxt = words[i + 1]
            # 如果前缀相同，且长的word排在短的word前面，可以直接返回 ""
            if len(cur) > len(nxt) and cur[:len(nxt)] == nxt: return ""
            
            minLen = min(len(cur), len(nxt))
            
            for j in range(minLen):
                # 找到第一个不同的字母
                if cur[j] != nxt[j]:
                    # nxt[j] 没有记录在 cur[j] 后面时才添加记录
                    if nxt[j] not in afterSet[cur[j]]:
                        beforeCnt[nxt[j]] += 1
                        afterSet[cur[j]].add(nxt[j])
                    break
                    
        dq = collections.deque()
        # 把字母前面字母数为0的先入队
        for c, cnt in beforeCnt.items():
            if cnt == 0:
                dq.append(c)
                
        # topo sort
        res = ""
        while dq:
            c = dq.popleft()
            res += c
            
            for afterChar in afterSet[c]:
                # 每添加一个 c，把 c 对应 afterSet中所有数的 beforeCnt 减 1，如果 beforeCnt 变成 0 就入队
                beforeCnt[afterChar] -= 1
                if beforeCnt[afterChar] == 0:
                    dq.append(afterChar)
                    
        return res if len(res) == len(beforeCnt) else ""
        
