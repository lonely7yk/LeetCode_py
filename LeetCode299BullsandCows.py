"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your 
friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates 
how many digits in said guess match your secret number exactly in both digit and position (called "bulls") 
and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend 
will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the 
bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""

import collections

# O(n)
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         counter = collections.Counter(secret)
#         n = len(secret)
#         bull = 0
#         cow = 0
        
#         # 先统计 bull
#         for i in range(n):
#             if secret[i] == guess[i]:
#                 counter[secret[i]] -= 1
#                 bull += 1
                
#         # 然后统计 cow
#         for i in range(n):
#             if secret[i] != guess[i]:
#                 if guess[i] in counter and counter[guess[i]] != 0:
#                     counter[guess[i]] -= 1
#                     cow += 1
                    
#         return str(bull) + 'A' + str(cow) + 'B'

# # 上面的 improvement
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         counter = collections.Counter(secret)
#         n = len(secret)
#         bull = 0
#         cow = 0
        
#         # 先统计 bull
#         for i, c in enumerate(guess):
#             if c in counter:
#                 if c == secret[i]:
#                     # 如果 counter[c] 等于 0，说明当前的 bull 被之前的 cow 占用了，扣除 cow
#                     if counter[c] == 0: cow -= 1
#                     else: counter[c] -= 1
#                     bull += 1
#                 else:
#                     if counter[c] > 0:
#                         counter[c] -= 1
#                         cow += 1

#         return '{}A{}B'.format(bull, cow)

# 最优解 One pass
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter = collections.defaultdict(lambda: 0)
        n = len(secret)
        bull = cow = 0

        for i in range(n):
            s, g = secret[i], guess[i]
            if s == g:
                bull += 1
            else:
                if counter[s] < 0: cow += 1
                if counter[g] > 0: cow += 1

                counter[s] += 1
                counter[g] -= 1

        return '{}A{}B'.format(bull, cow) 

