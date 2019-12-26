'''
You are given a string, s, and a list of words, words, that are all of 
the same length. Find all starting indices of substring(s) in s that is 
a concatenation of each word in words exactly once and without any 
intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]

Explanation: Substrings starting at index 0 and 9 are "barfoo" and 
"foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''

from typing import List
from collections import defaultdict

class Solution:
    # 528ms 43.95%
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or len(s) == 0 or len(words) == 0: return []

        wordCount = defaultdict(lambda: 0)
        strLen = len(words[0])
        res = []

        for word in words:
            wordCount[word] += 1

        for i in range(0, len(s) - strLen * len(words) + 1):
            wordNum = 0
            seen = defaultdict(lambda: 0)
            while wordNum < len(words):
                currWord = s[i + wordNum * strLen : i + (wordNum + 1) * strLen]
                if currWord in words:
                    seen[currWord] += 1
                    if seen[currWord] > wordCount[currWord]: break
                else:
                    break
                wordNum += 1
            if wordNum == len(words):
                res.append(i)
        return res


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]

    # s = "wordgoodgoodgoodbestword"
    # words = ["word","good","best","word"]
    res = Solution().findSubstring(s, words)
    print(res)


