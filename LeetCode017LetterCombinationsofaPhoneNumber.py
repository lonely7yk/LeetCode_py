"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the 
number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not 
map to any letters.

1     2abc 3def
4ghi  5jkl 6mno
7pqrs 8tuv 9wxyz

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

from typing import List
import collections

class Solution:
    # # DFS: O(4^n) 20ms 97%
    # def letterCombinations(self, digits: str) -> List[str]:
    #     def findCombinationsDFS(curr, res, idx, digits, digitMap):
    #         if idx == len(digits):
    #             res.append(curr)
    #             return

    #         digit = digits[idx]
    #         for c in digitMap[digit]:
    #             findCombinationsDFS(curr + c, res, idx + 1, digits, digitMap)

    #     if not digits: return []

    #     curr = ""
    #     res = []
    #     digitMap = {
    #         '2':'abc',
    #         '3':'def',
    #         '4':'ghi',
    #         '5':'jkl',
    #         '6':'mno',
    #         '7':'pqrs',
    #         '8':'tuv',
    #         '9':'wxyz'
    #     }
    #     findCombinationsDFS(curr, res, 0, digits, digitMap)
    #     return res

    # BFS: O(4^n) 24ms 87%
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        queue = collections.deque([""])
        digitMap = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        for i in range(len(digits)):
            digit = digits[i]

            while i == len(queue[0]):
                s = queue.popleft()
                for c in digitMap[digit]:
                    queue.append(s + c)

        return list(queue)



if __name__ == '__main__':
    digits = "23"
    res = Solution().letterCombinations(digits)
    print(res)