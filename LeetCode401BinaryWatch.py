"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom 
represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all 
possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
- The order of output does not matter.
- The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
- The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, 
it should be "10:02".
"""

from typing import List

class Solution:
    # DFS: 24ms 90%
    # 注意精度问题
    # def readBinaryWatch(self, num: int) -> List[str]:
    #     def dfs(res, time, num, start, timeList):
    #         # round 很关键
    #         if round((time - int(time)) * 100) > 59 or int(time) > 11: return
            
    #         if num == 0:
    #             hour = int(time)
    #             minute = round(100 * (time - hour)) # round 很关键
    #             hourStr = str(hour)
    #             minuteStr = str(minute) if minute >= 10 else '0' + str(minute)
    #             res.append(hourStr + ':' + minuteStr)
    #             return
            
    #         for i in range(start, len(timeList)):
    #             dfs(res, time + timeList[i], num - 1, i + 1, timeList)
            
            
    #     timeList = [8, 4, 2, 1, 0.32, 0.16, 0.08, 0.04, 0.02, 0.01];
    #     res = []
    #     dfs(res, 0, num, 0, timeList)
    #     return res

    # Bit operation: 32ms 57%
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []

        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    res.append('%d:%02d' % (h, m))

        return res
        
if __name__ == '__main__':
    res = Solution().readBinaryWatch(2)
    print(res)
