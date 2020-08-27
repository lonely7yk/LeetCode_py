"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

from typing import List
import collections

# HashMap: O(nk)   n is the length of strings, k is the average length of all strings
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groupMap = collections.defaultdict(list)
        
        for string in strings:
            curr = []
            for i in range(1, len(string)):
                diff = ord(string[i]) - ord(string[i - 1])
                if diff < 0: diff += 26
                curr.append(diff)
            
            groupMap[tuple(curr)].append(string)
            
        return groupMap.values()
        
