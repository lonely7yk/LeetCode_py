"""
Write a class StockSpanner which collects daily price quotes for some stock, and returns the 
span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days 
(starting from today and going backwards) for which the price of the stock was less than 
or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], 
then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
"""

# 每次加入价格就把 price 和 span 都保存下来，加入新价格查询上一个 price 是否小于当前 price，
# 如果小于，加到 span 上，并继续往前查找，知道找到比当前 price 高的 price
# class StockSpanner:

#     def __init__(self):
#         self.prices = []    # 保存每天的股票价格
#         self.spans = []     # 保存每天的股票对应的 span

#     def next(self, price: int) -> int:
#         self.prices.append(price)

#         span = 1
#         if len(self.spans) != 0:
#             # 从当前添加价格的前一个价格开始比较
#             idx = len(self.spans) - 1
#             while idx > -1:
#                 # 如果 price 小于该天的价格，则不需要继续往前算了
#                 if self.prices[idx] > price: break

#                 # 如果 price 大于该天价格，把小于该天价格的天数先加上，然后更新 idx 到小于该天连续天数的前一天
#                 span += self.spans[idx]
#                 idx = idx - self.spans[idx]

#         self.spans.append(span)
#         return span

# 上述方法的改进，每次把比当前天价格低的price和span出栈，这样可以使 stack 存储元素更少
class StockSpanner:

    def __init__(self):
        self.stack = []     # 二维 list，第一个元素存 price， 第二个元素存 span

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[-1]

        self.stack.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
