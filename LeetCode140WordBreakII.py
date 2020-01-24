"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s 
to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

from typing import List

class Solution:
    # DFS+HashMap: 80ms 27%
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s, wordSet, map_):
            if s in map_:
                return map_[s]

            res = []
            for i in range(1, len(s) + 1):
                if s[:i] in wordSet:
                    # 这句相当于边界条件
                    if i == len(s):
                        res.append(s[:i])
                    else:
                        afterStrs = dfs(s[i:], wordSet, map_)
                        for afterStr in afterStrs:
                            res.append(s[:i] + " " + afterStr)

            map_[s] = res   # map 用来保存 s 对应的字符串 list
            return res

        wordSet = set(wordDict)
        return dfs(s, wordSet, {})

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]

    res = Solution().wordBreak(s, wordDict)
    print(res)
        
