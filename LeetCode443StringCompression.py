"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 

Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""

from typing import List

# Two Pointer: O(n) - O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        r = 0   # 读指针
        w = 0   # 写指针
        n = len(chars)
        
        while r < n:
            # 当前字符
            currChar = chars[r]
            # 统计连续字符个数
            cnt = 0
            while r < n and chars[r] == currChar:
                r += 1
                cnt += 1
                    
            chars[w] = currChar
            w += 1

            # 如果 cnt 为 1，则不添加到 chars 中
            cnt_str = str(cnt) if cnt != 1 else ''
            for c in cnt_str:
                chars[w] = c
                w += 1
                
        return w
            
chars = ["a","a","b","b","c","c","c"]
res = Solution().compress(chars)
print(chars)
print(res)