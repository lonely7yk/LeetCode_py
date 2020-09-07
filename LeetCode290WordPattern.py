"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""

# # Two HashMap: O(n)
# class Solution:
#     def wordPattern(self, pattern: str, str: str) -> bool:
#         words = str.split()
#         if len(words) != len(pattern): return False
        
#         n = len(pattern)
#         patternWordMap = dict()
#         wordPatternMap = dict()
        
#         for i in range(n):
#             c = pattern[i]
#             word = words[i]
#             if c not in patternWordMap and word not in wordPatternMap:
#                 patternWordMap[c] = word
#                 wordPatternMap[word] = c
#             elif c not in patternWordMap and word in wordPatternMap:
#                 return False
#             elif c in patternWordMap and word not in wordPatternMap:
#                 return False
#             else:
#                 if patternWordMap[c] != word or wordPatternMap[word] != c: return False
                
#         return True
        

# One HashMap: O(n)
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern): return False
        
        n = len(pattern)
        idxMap = dict() # value 为 char 或 word 第一次出现的索引
        
        for i in range(n):
            c = pattern[i]
            word = words[i]
            
            charKey = 'char_{}'.format(c)
            wordKey = 'word_{}'.format(word)
            
            if charKey not in idxMap:
                idxMap[charKey] = i
                
            if wordKey not in idxMap:
                idxMap[wordKey] = i
                
            if idxMap[charKey] != idxMap[wordKey]: return False
            
        return True
