"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1: return True
        
        if word[0].isupper():
            # 如果首字母大写，那么只要保证后面所有字母都是大写，或都是小写
            last = word[1].isupper()
            for i in range(2, len(word)):
                curr = word[i].isupper()
                if curr != last: return False
                last = curr
            return True
        else:
            # 如果首字母小写，那么要保证后面所有字母都是小写
            for i in range(1, len(word)):
                if word[i].isupper(): return False
            return True
        
