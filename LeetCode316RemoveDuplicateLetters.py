"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make 
sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""


# Stack: O(n)
# https://leetcode.com/problems/remove-duplicate-letters/discuss/76769/Java-solution-using-Stack-with-comments
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        stack = []
        visited = set()
        
        for c in s:
            counter[c] -= 1
            # 已经添加，直接跳过
            if c in visited: continue
            
            # 如果 c 比栈顶的小，且栈顶元素在后面还存在，则排除栈顶元素
            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                visited.remove(stack[-1])
                stack.pop()
                
            stack.append(c)
            visited.add(c)
            
        return ''.join(stack)
        
