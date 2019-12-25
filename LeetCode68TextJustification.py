"""
Given an array of words and a width maxWidth, format the text such that 
each line has exactly maxWidth characters and is fully (left and right) 
justified.

You should pack your words in a greedy approach; that is, pack as many 
words as you can in each line. Pad extra spaces ' ' when necessary so 
that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots 
on the right.

For the last line of text, it should be left justified and no extra 
space is inserted between words.

Note:

1. A word is defined as a character sequence consisting of non-space 
characters only.
2. Each word's length is guaranteed to be greater than 0 and not exceed 
maxWidth.
3. The input array words contains at least one word.

Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

from typing import List

class Solution:
    # 32ms 70%
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currLen = len(words[0]) # 当前行的长度，每个单词加一个空格
        currList = [words[0]]   # 当前行的 words
        res = []

        for i in range(1, len(words)):
            word = words[i]
            tmp = currLen + len(word) + 1
            if tmp <= maxWidth:
                currLen = tmp
                currList.append(word)
            else:
                extraSpaceNum = maxWidth - currLen  # 除了每个单词一个空格，还剩下多少空格
                k = len(currList)
                line = ""
                for i in reversed(range(1, k)):
                    line = " " * (extraSpaceNum // (k - 1) + 1) + currList[i] + line
                    extraSpaceNum -= extraSpaceNum // (k - 1)
                    k -= 1

                line = currList[0] + line
                if len(currList) == 1: line = line + " " * (maxWidth - len(line))   # 如果结尾只有一个单词，要在结尾补空格
                res.append(line)

                currLen = len(word)
                currList = [word]

        lastLine = currList[0]
        for i in range(1, len(currList)):
            lastLine += " " + currList[i]
        lastLine = lastLine + " " * (maxWidth - len(lastLine))  # 最后一行结尾补空格
        res.append(lastLine)

        return res

if __name__ == '__main__':
    # words = ["Science","is","what","we","understand","well","enough","to","explain",
    #      "to","a","computer.","Art","is","everything","else","we","do"]
    # maxWidth = 20

    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16

    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # maxWidth = 16

    res = Solution().fullJustify(words, maxWidth)
    for line in res:
        print(line)


