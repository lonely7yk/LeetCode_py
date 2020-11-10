"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""

from typing import List
import collections


# # Categorize by Count
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         memo = collections.defaultdict(list)
        
#         for s in strs:
#             cnt = [0 for i in range(26)]
#             for c in s:
#                 cnt[ord(c) - ord('a')] += 1
                
#             memo[tuple(cnt)].append(s)
            
#         return memo.values()
        

# Categorize by Sorted String
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = collections.defaultdict(list)
        
        for s in strs:
            memo[tuple(sorted(s))].append(s)
            
        return memo.values()
        
