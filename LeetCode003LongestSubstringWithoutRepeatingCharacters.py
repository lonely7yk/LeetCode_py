"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# # Sliding Window: O(n)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         strSet = set()
#         left = 0
#         right = 0
#         res = 0
        
#         while right < n:
#             if s[right] not in strSet:
#                 strSet.add(s[right])
#                 right += 1
#                 res = max(res, right - left)
#             else:
#                 repeat = s[right]
#                 while s[left] != repeat:
#                     strSet.remove(s[left])
#                     left += 1
#                 left += 1
#                 right += 1
                
#         return res


# Sliding window improve: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        idxMap = dict()
        left = 0
        right = 0
        res = 0
        
        while right < n:
            if s[right] not in idxMap:
                idxMap[s[right]] = right
                right += 1
            else:
                repeat = s[right]
                idx = idxMap[repeat]
                # 这句是关键，确保已经抛弃的 idx 不会被使用（抛弃指 left 前面的 idx）
                left = max(left, idx + 1)
                idxMap[repeat] = right
                right += 1
                
            res = max(res, right - left)
                
        return res
                
            
        
                
            
        
