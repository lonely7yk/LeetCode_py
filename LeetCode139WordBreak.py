"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

from typing import List

class Solution:
    # # DP: O(n^2)
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     dp = [False for i in range(len(s) + 1)]
    #     dp[0] = True
    #     wordSet = set(wordDict)
        
    #     for i in range(1, len(s) + 1):
    #         for j in range(1, i + 1):
    #             if dp[i - j] and s[i - j:i] in wordSet:
    #                 dp[i] = True
    #                 break
                    
    #     return dp[-1]

    # DFS + HashMap
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s, wordSet, dic):
            if not s: return True
            if s in dic: return dic[s]
            
            for i in range(1, len(s) + 1):
                if s[:i] in wordSet and dfs(s[i:], wordSet, dic):
                    dic[s] = True
                    return True
                
            dic[s] = False
            return False
        
        dic = {}
        wordSet = set(wordDict)
        return dfs(s, wordSet, dic)