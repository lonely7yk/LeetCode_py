"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to 
endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that beginWord 
is not a transformed word.

Note:

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" 
-> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible 
transformation.
"""

from typing import List
from collections import deque
import string

class Solution:
    # # BFS: O(n^3) TLE
    # # 每个单词单独判断是否能转换，时间复杂度太高
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     queue = deque()
    #     wordSet = set(wordList)
    #     cnt = 0

    #     queue.append(beginWord)

    #     while len(queue) != 0:
    #         cnt += 1
    #         queueLen = len(queue)

    #         for _ in range(queueLen):
    #             curr = queue.popleft()

    #             for word in list(wordSet):
    #                 if self.canTransfer(curr, word):
    #                     if word == endWord: return cnt + 1

    #                     queue.append(word)
    #                     wordSet.remove(word)
    #     return 0

    # def canTransfer(self, word1, word2):
    #     flag = False    # 表示是否碰到过相同字母
    #     n = len(word1)
    #     for i in range(n):
    #         if word1[i] != word2[i]:
    #             if flag: return False
    #             else: flag = True
    #     return flag

    # BFS: O(n^2 * 26) 464ms 35.63%
    # 参考：https://leetcode.com/problems/word-ladder/discuss/40707/C%2B%2B-BFS
    # 参考：https://leetcode.com/problems/word-ladder/discuss/157376/Python-(BFS)-tm
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        alpha = string.ascii_lowercase
        queue = deque([beginWord])
        wordLen = len(beginWord)
        cnt = 0

        while queue:
            queueLen = len(queue)
            cnt += 1

            for _ in range(queueLen):
                curr = queue.popleft()
                if curr == endWord: return cnt

                for i in range(wordLen):
                    for c in alpha:
                        # 使用 26 个字母替换掉当前字母，看单词是否在 wordSet 中
                        newWord = curr[:i] + c + curr[i + 1:]
                        if newWord in wordSet:
                            wordSet.remove(newWord)
                            queue.append(newWord)
        return 0

if __name__=='__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","dot","dog","lot","log"]

    res = Solution().ladderLength(beginWord, endWord, wordList)
    print(res)
