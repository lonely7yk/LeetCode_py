"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.

Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""

from typing import List
import collections


class TrieNode:
    def __init__(self):
        self.words = []
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        p = self.root

        for c in word:
            p = p.children[c]
            p.words.append(word)

    def getWordsWithPrefix(self, prefix):
        p = self.root
        for c in prefix:
            p = p.children[c]

        return p.words

# Trie + BackTracking
# 用 trie 记录每个前缀对应的 words。对于每一次 backtrack，找到下一层的前缀，根据前缀找到所有单词候选，然后依次回溯
# https://leetcode.com/problems/word-squares/discuss/91333/Explained.-My-Java-solution-using-Trie-126ms-1616
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(curr, res, step, n):
            # step == n 说明已生成 word square
            if step == n:
                res.append(curr)
                return

            prefix = ""
            for i in range(step):
                prefix += curr[i][step]

            # 找到所有前缀为 prefix 的单词
            wordsWithPrefix = trie.getWordsWithPrefix(prefix)
            for word in wordsWithPrefix:
                dfs(curr + [word], res, step + 1, n)

        res = []
        for word in words:
            dfs([word], res, 1, len(word))

        return res


words = ["area","lead","wall","lady","ball"]
res = Solution().wordSquares(words)
print(res)

