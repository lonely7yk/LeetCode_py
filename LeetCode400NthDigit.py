'''
Find the nth digit of the infinite integer s
equence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 
is a 0, which is part of the number 10.
'''

class Solution:
    # 28ms 81%
    def findNthDigit(self, n: int) -> int:
        digit = 1
        # 每十位的总个数是有规律的即 (9*10^n)*n （n是位数）
        while n > 9 * 10 ** (digit - 1) * digit:
            n -= 9 * 10 ** (digit - 1) * digit
            digit += 1

        start = 10 ** (digit - 1)
        divide = n / digit
        remainder = n % digit

        if remainder == 0:
            return int((start + divide - 1) % 10)
        else:
            return int((start + divide) // 10 ** (digit - remainder) % 10)

if __name__ == '__main__':
    solution = Solution()
    print(solution.findNthDigit(15))
