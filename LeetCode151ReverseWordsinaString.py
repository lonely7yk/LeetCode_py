"""
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(reversed(s.split()))


# in-place
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        s = list(s)
        idx = 0
        n = len(s)
        reverse(s, 0, n - 1)    # reverse the string

        i = 0
        while i < n:
            if s[i] != ' ':
                if idx != 0: 
                    s[idx] = ' '
                    idx += 1

                j = i
                while j < n and s[j] != ' ': 
                    s[idx] = s[j]
                    j += 1
                    idx += 1

                reverse(s, idx - (j - i), idx - 1)
                i = j
            i += 1

        return "".join(s[:idx])

# s = "the sky is blue"
s = "  hello world!  "
res = Solution().reverseWords(s)
print(res)
