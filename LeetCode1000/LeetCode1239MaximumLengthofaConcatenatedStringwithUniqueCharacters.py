"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""

# # Brute Force: O(2^n)
# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         def dfs(curr, idx):
#             if idx == len(arr): return len(curr)
#             if len(set(arr[idx])) != len(arr[idx]): return dfs(curr, idx + 1)
            
#             maxLen = dfs(curr, idx + 1)
#             if not set(curr) & set(arr[idx]):
#                 maxLen = max(maxLen, dfs(curr + arr[idx], idx + 1))
                
#             return maxLen
        
#         return dfs("", 0)


# Brute Force iterative
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [set()]
        
        for a in arr:
            if len(set(a)) != len(a): continue
            a = set(a)
            
            for i in range(len(res) - 1, -1, -1):
                if not res[i] & a:
                    res.append(a | res[i])
                    
        return max([len(a) for a in res])

        
        
