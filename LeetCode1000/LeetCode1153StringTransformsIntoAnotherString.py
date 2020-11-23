"""
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing 
zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.

Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 

Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.
"""


# 直接扫一遍，从 str1 映射到 str2，如果一个字母映射多个字母则返回 False
# 注意，因为映射需要一个中间变量，所以 str2 中最多只能有 25 个字母（除了 str1 == str2）
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True
        dic = dict()
        
        for c1, c2 in zip(str1, str2):
            if c1 not in dic:
                dic[c1] = c2
            else:
                if dic[c1] != c2: return False
                
        return len(set(str2)) < 26
        
