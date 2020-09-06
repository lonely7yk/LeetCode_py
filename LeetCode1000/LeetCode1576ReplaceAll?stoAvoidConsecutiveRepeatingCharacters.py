"""
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower
case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the
non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution,
return any of them. It can be shown that an answer is always possible with the given constraints.

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid
modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will
consist of consecutive repeating characters in "ubvvw" and "ubvww".

Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"

Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"

Constraints:

1 <= s.length <= 100

s contains only lower case English letters and '?'.
"""

import string


# O(n)
class Solution:
    def modifyString(self, s: str) -> str:
        charArr = list(s)
        n = len(s)

        for i, c in enumerate(charArr):
            # 只有 c 等于 '?' 时才改变 c
            if c == '?':
                # 直接遍历所有字母
                for tmp in string.ascii_lowercase:
                    # 不能与前一个字母一样
                    if i >= 0 and tmp == charArr[i - 1]: continue
                    # 不能与后一个字母一样
                    if i < n - 1 and tmp == charArr[i + 1]: continue

                    # 一旦赋值就 break
                    charArr[i] = tmp
                    break

        return ''.join(charArr)
