"""
Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

Example 1:

Input: digits = [8,1,9]
Output: "981"

Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
Example 4:

Input: digits = [0,0,0,0,0,0]
Output: "0"

Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
The returning answer must not contain unnecessary leading zeros.
"""

from typing import List

class Solution:
    # O(n): 88ms 100%
    # 3的倍数的数必须满足所有位数加起来是3的倍数
    # 如果加起来是 %3=1 说明要减去一个 %3=1 或者两个 %3=2
    # 如果加起来是 %3=2 说明要减去一个 %3=2 或者两个 %3=1
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # 使用map_生成字符串
        def generateStr(map_):
            res = ""
            for i in range(9, 0, -1):
                res += str(i) * map_[i]

            # res 为空，说明1-9都没值
            if res == "": 
                return "0" if map_[0] else ""
            res += "0" * map_[0]
            return res

        # 删除num个 map_ 中余数为 remainder 的数
        def delMap(map_, num, remainder):
            tmp = {1: [1, 4, 7], 2: [2, 5, 8]}
            l = tmp[remainder]
            cnt = 0
            for i in l:
                while map_[i]:
                    map_[i] -= 1
                    cnt += 1
                    if cnt == num: break
                if cnt == num: break


        map_ = [0 for i in range(10)]
        s = 0

        for digit in digits:
            map_[digit] += 1
            s += digit

        r1 = map_[1] + map_[4] + map_[7]
        r2 = map_[2] + map_[5] + map_[8]

        if s % 3 == 0:
            return generateStr(map_)
        elif s % 3 == 1:
            if r1 >= 1:
                delMap(map_, 1, 1)
                return generateStr(map_)
            elif r2 >= 2:
                delMap(map_, 2, 2)
                return generateStr(map_)
        elif s % 3 == 2:
            if r2 >= 1:
                delMap(map_, 1, 2)
                return generateStr(map_)
            elif r1 >= 2:
                delMap(map_, 2, 1)
                return generateStr(map_)

        return ""


if __name__ == '__main__':
    digits = [0,0,0]
    res =  Solution().largestMultipleOfThree(digits)
    print(res)
