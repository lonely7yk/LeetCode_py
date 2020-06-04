"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to 
city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each 
city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in 
each city.

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""

# # O(nlogn) : 对飞去 A 和飞去 B 的插值的绝对值进行从大到小排序，
# # 排在前面的说明选择小的 cost 对总 cost 的效益最高。
# # 如果其中一个城市去满了就把剩下的安排到另一个城市
# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         costs.sort(key=lambda x: -abs(x[0] - x[1]))
#         n = len(costs) // 2
#         ANum = 0
#         BNum = 0
#         res = 0
        
#         for cost in costs:
#             if ANum == n:
#                 res += cost[1]
#                 BNum += 1
#             elif BNum == n:
#                 res += cost[0]
#                 ANum += 1
#             else:
#                 if cost[0] < cost[1]:
#                     res += cost[0]
#                     ANum += 1
#                 else:
#                     res += cost[1]
#                     BNum += 1
                    
#         return res
                
# O(nlogn) : 先把城市 A 的所有 cost 加起来，然后把城市 B 的 cost 减城市 A 的 cost 组成一个数组 Diff
# 每加上一个 Diff 的元素，就相当于减去一个 A 并加上对应的 B。因此只要将 Diff 从小到大排序然后加上前一般
# 就相当于去城市 A n个人，城市 B n个人，而且 cost 综合最小。
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ACosts = [x for x,y in costs]
        diffs = [y - x for x,y in costs]
        diffs.sort()
        return sum(ACosts) + sum(diffs[:len(diffs) // 2])

