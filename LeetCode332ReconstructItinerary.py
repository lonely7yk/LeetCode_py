# """
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus,
# the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest
# lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller
# lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.
# """

from typing import List
import collections
import heapq
import bisect

# # DFS: 200ms 5%
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         def dfs(curr, res, tickets, start):
#             if res: return
            
#             if not tickets:
#                 res.append(list(curr))
#                 return
            
#             for i in range(len(tickets)):
#                 ticket = tickets[i]
#                 if ticket[0] == start:
#                     tmp = list(tickets)
#                     tmp.pop(i)
#                     dfs(curr + [ticket[1]], res, tmp, ticket[1])
           
#         res = []
#         curr = ["JFK"]
#         # 根据 ticket 的目的地进行排序，这样后面遍历的话会优先遍历到字母顺序小的目的地
#         tickets.sort(key=lambda x : x[1])
#         dfs(curr, res, tickets, "JFK")
        
#         return res[0]

# DFS Bottom Up + Heap: 80ms 71%
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)

        for ticket in tickets:
            heapq.heappush(d[ticket[0]], ticket[1])

        def dfs(from_, res):
            while d[from_]:
                to_ = heapq.heappop(d[from_])
                dfs(to_, res)

            # 走完循环说明已经没有后续的节点，可以把这个节点放在 res 最前面，表示当前的最后节点
            res.insert(0, from_)

        res = []
        dfs("JFK", res)
        return res

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
res = Solution().findItinerary(tickets)
print(res)

