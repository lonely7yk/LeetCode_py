'''
A character in UTF8 can be from 1 to 4 bytes long, subjected to 
the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, 
followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used 
to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
'''
from typing import List


class Solution:
    # # String Manipulation: 128ms 61.6%
    # def validUtf8(self, data: List[int]) -> bool:
    #     if len(data) == 0: return False
    #     expect = 0      # 表示后面应该还有多少个 10 开头的字节

    #     for num in data:
    #         curr = self.decimal2binary(num)
    #         zeroIdx = curr.find('0')
    #         if zeroIdx == -1 or zeroIdx >= 5:
    #             return False                

    #         if expect != 0:         # expect != 0时，当前字节必须以 10 开头，否则返回 False
    #             if zeroIdx != 1:
    #                 return False
    #             else:
    #                 expect -= 1
    #         else:                   # expect == 0时，当前字节不能以 10 开头
    #             if zeroIdx == 0:
    #                 expect = 0
    #             elif zeroIdx == 1:
    #                 return False
    #             else:
    #                 expect = zeroIdx - 1

    #     return expect == 0

    # def decimal2binary(self, decimal: int) -> str:
    #     # 将十进制数转成 8 位的二进制字符串
    #     tmp = str(bin(decimal))[2:]
    #     return tmp.zfill(8)

    # # Bit Operation: 96ms 99%
    # def validUtf8(self, data: List[int]) -> bool:
    #     expect = 0

    #     for num in data:
    #         if 128 <= num <= 191:   # 表示 num 在 1000 0000~1011 1111
    #             if expect == 0:
    #                 return False
    #             else:
    #                 expect -= 1
    #         else:
    #             if expect != 0:
    #                 return False
    #             elif num >= 248:    # 1111 1000
    #                 return False
    #             elif num >= 240:    # 1111 0000
    #                 expect = 3
    #             elif num >= 224:    # 1110 0000
    #                 expect = 2
    #             elif num >= 192:    # 1100 0000
    #                 expect = 1
    #             else:
    #                 expect = 0

    #     return expect == 0


    # My Solution: O(n)
    class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def calcBytes(num):
            ranges = [(0, 128), (192, 224), (224, 240), (240, 248)]
            for i, r in enumerate(ranges):
                if r[0] <= num < r[1]: return i + 1
                
            return -1
                
        def check(num):
            return 128 <= num < 192
        
        i = 0
        n = len(data)
        while i < n:
            num = data[i]
            b = calcBytes(num)
            if b == -1: return False
            if i + b - 1 >= n: return False
            
            for j in range(i + 1, i + b):
                if not check(data[j]): return False
                
            i = i + b
                
        return True


if __name__ == '__main__':
    solution = Solution()
    data = [197, 130, 1]
    # data = [145]
    print(solution.validUtf8(data))
