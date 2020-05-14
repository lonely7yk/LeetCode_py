"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

class Solution:
    # 32ms 100%
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # 判断是否是闰年
        def judge(year):
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                return True
            else:
                return False

        # 计算该天到年初一共多少天
        def countDay(y, m, d):
            res = 0
            months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if judge(y): months[2] += 1
            for i in range(1, m):
                res += months[i]

            res += d
            return res

        if date1 > date2:
            date1, date2 = date2, date1

        y1, m1, d1 = [int(x) for x in date1.split('-')]
        y2, m2, d2 = [int(x) for x in date2.split('-')]

        days = 0

        count1 = countDay(y1, m1, d1)
        count2 = countDay(y2, m2, d2)

        days = count2 - count1

        # 从 y1 年初到 y2 年初一共多少天
        for i in range(y1, y2):
            if judge(i):
                days += 366
            else:
                days += 365

        return days

if __name__ == '__main__':
    date1 = "1971-06-29"
    date2 = "2010-09-23"

    res = Solution().daysBetweenDates(date1, date2)
    print(res)
