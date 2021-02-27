"""
Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do 
is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out 
the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). 
There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the 
party. If there is no celebrity, return -1.

Example 1:

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, 
otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:

Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

Constraints:

n == graph.length
n == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1

Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True

import collections

# Logical Deduction: https://leetcode.com/problems/find-the-celebrity/discuss/71227/Java-Solution.-Two-Pass
# O(n)
# The first loop is to find the candidate as the author explains. In detail, suppose the candidate after the first for loop is person k, 
# it means 0 to k-1 cannot be the celebrity, because either they know any candidate or they are not known by 0 to k-1. Also, since k knows no one between k+1 and
# n-1, k+1 to n-1 can not be the celebrity either. Therefore, k is the only possible celebrity, if there exists one.
# The remaining job is to check if k indeed does not know any other persons and all other persons know k.
# To this point, I actually realize that we can further shrink the calling of knows method. For example, we don't need to check if k knows k+1 
# to n-1 in the second loop, because the first loop has already done that.
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
                
        cnt = 0
        for i in range(n):
            if i == candidate: continue
            if knows(candidate, i): return -1
            if knows(i, candidate): cnt += 1
                
        return candidate if cnt == n - 1 else -1

        
