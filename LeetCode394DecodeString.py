'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside 
the square brackets is being repeated exactly k times. Note that k is 
guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any 
digits and that digits are only for those repeat numbers, k. For example, 
there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution:
    # Stack: 20ms 98%
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        currStr = ''
        currNum = 0

        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                currNum = currNum * 10 + int(s[i])
            elif s[i] == '[':
                numStack.append(currNum)
                strStack.append(currStr)
                currStr = ''
                currNum = 0
            elif s[i] == ']':
                popStr = strStack.pop()
                popNum = numStack.pop()
                currStr = popStr + currStr * popNum
            else:
                currStr += s[i]

        return currStr


if __name__ == '__main__':
    solution = Solution()
    s = '100[leet]'
    print(solution.decodeString(s))
