"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" 
cells are those horizontally or vertically neighboring. The same letter cell may not be used 
more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""

from typing import List
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        p = self.root
        for c in word:
            p = p.children[c]
        p.isWord = True

# Trie + DFS
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(trieNode, i, j, res, currWord):
            if trieNode.isWord: 
                res.append(currWord)
                trieNode.isWord = False # 防止重复

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): return
            if board[i][j] == '#': return

            c = board[i][j]
            board[i][j] = '#'   # 将 board[i][j] 置为 '#' 表示已经访问过，代替 visited

            if c in trieNode.children:
                nxtWord = currWord + c
                dfs(trieNode.children[c], i - 1, j, res, nxtWord)
                dfs(trieNode.children[c], i + 1, j, res, nxtWord)
                dfs(trieNode.children[c], i, j - 1, res, nxtWord)
                dfs(trieNode.children[c], i, j + 1, res, nxtWord)

            board[i][j] = c     # DFS 后要记得把 board[i][j] 变回原来的字母


        trie = Trie()
        for word in words:
            trie.addWord(word)

        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                dfs(trie.root, i, j, res, '')

        return res



# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]

# board = [["a", "b"]]
# words = ["a", "b"]

board = [
["b","a","a","b","a","b"],
["a","b","a","a","a","a"],
["a","b","a","a","a","b"],
["a","b","a","b","b","a"],
["a","a","b","b","a","b"],
["a","a","b","b","b","a"],
["a","a","b","a","a","b"]]
words = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
# words = ["aabbbbabbaababaaaabababbaaba"]

res = Solution().findWords(board, words)
print(res)

