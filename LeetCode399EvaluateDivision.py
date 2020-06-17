'''
Equations are given in the format A / B = k, where A and B are variables 
represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, 
return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, 
vector<pair<string, string>> queries , where equations.size() == values.size(), 
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result 
in no division by zero and there is no contradiction.
'''

from typing import List
import collections
import itertools

# class Solution:
#     # # dict: 20ms 99%
#     # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#     #     equalDict = dict()
#     #     charSet = set()
#     #     res = []

#     #     for equation, value in zip(equations, values):
#     #         charSet.add(equation[0])
#     #         charSet.add(equation[1])
#     #         equalDict[tuple(equation)] = value
#     #         equalDict[(equation[1], equation[0])] = 1 / value
#     #         # 每加入一个 query 还要看前面是否能和刚加入的 query 匹配
#     #         # 这里要加 list 不然会报 RuntimeError
#     #         for k, v in list(equalDict.items()):
#     #             if k[0] == equation[1]:
#     #                 equalDict[(equation[0], k[1])] = v * value
#     #                 equalDict[(k[1], equation[0])] = 1 / (v * value)
#     #             elif k[0] == equation[0]:
#     #                 equalDict[(equation[1], k[1])] = v / value
#     #                 equalDict[(k[1], equation[1])] = value / v

#     #     # 自己和自己除等于 1.0
#     #     for char in charSet:
#     #         equalDict[(char, char)] = 1.0

#     #     for query in queries:
#     #         first = query[0]
#     #         last = query[1]
#     #         # 如果query中有字母不在 set 中说明不能匹配
#     #         if first not in charSet or last not in charSet:
#     #             res.append(-1.0)
#     #             continue

#     #         for char in charSet:
#     #             if (first, char) in equalDict and (char, last) in equalDict:
#     #                 res.append(equalDict[(first, char)] * equalDict[(char, last)])
#     #                 break
#     #         else:   # 如果没有 break 说明不能配对
#     #             res.append(-1.0)

#     #     return res

#     # Floyd: 28ms 87%
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         quot = collections.defaultdict(dict)
#         for (first, last), val in zip(equations, values):
#             quot[first][first] = quot[last][last] = 1.0
#             quot[first][last] = val
#             quot[last][first] = 1 / val

#         # 这两个循环是一样的
#         # for k in quot:
#         #     for i in quot[k]:
#         #         for j in quot[k]:
#         #             quot[i][j] = quot[i][k] * quot[k][j]

#         for k, i, j in itertools.permutations(quot, 3):
#             if k in quot[i] and k in quot[j]:
#                 quot[i][j] = quot[i][k] * quot[k][j]

#         return [quot[first].get(last, -1.0) for (first, last) in queries]

# graph + BFS: 32ms 52%
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 使用 BFS 来找 first -> last 的结果
        def findPath(first, last, graph):
            if first not in graph or last not in graph: return -1

            # 第一个数为当前结点，第二个是数为到当前结点的运算结果
            dq = collections.deque([(first, 1.0)])
            visited = set() # 保存已经访问过的节点

            while dq:
                curr, point = dq.popleft()
                # 如果当前结点已经到了结果节点，则直接返回结果
                if curr == last: return point
                visited.add(curr)

                # 遍历当前结点的所有邻接节点
                for nxt, value in graph[curr]:
                    # 只添加未访问的节点
                    if nxt not in visited:
                        dq.append((nxt, point * value))

            return -1


        graph = collections.defaultdict(list)

        # 把运算想象成图，key 为除数，value 存放被除数和值
        for (first, last), value in zip(equations, values):
            graph[first].append((last, value))
            graph[last].append((first, 1 / value))

        return [findPath(first, last, graph) for first, last in queries]
        

if __name__ == '__main__':
    # equations = [ ["a", "b"], ["b", "c"] ]
    # values = [2.0, 3.0]
    # queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    solution = Solution()
    res = solution.calcEquation(equations, values, queries)
    print(res)


