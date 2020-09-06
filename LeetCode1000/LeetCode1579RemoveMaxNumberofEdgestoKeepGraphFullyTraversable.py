"""
Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui
and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully
traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can
reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed
by Alice and Bob.

Example 1:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob.
Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

Example 2:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

Example 3:

Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1.
Therefore it's impossible to make the graph fully traversable.

Constraints:

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
All tuples (typei, ui, vi) are distinct.
"""

from typing import List

# # Union Find
# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         # union find 的 find 方法
#         def find(roots, x):
#             if x == roots[x]:
#                 return x
#             else:
#                 roots[x] = find(roots, roots[x])
#                 return roots[x]
#
#         pairs1 = []
#         pairs2 = []
#         pairs3 = []
#
#         # 分成三类
#         for type, x, y in edges:
#             if type == 1:
#                 pairs1.append((x, y))
#             elif type == 2:
#                 pairs2.append((x, y))
#             else:
#                 pairs3.append((x, y))
#
#         roots = [i for i in range(n + 1)]
#         # root 的集合
#         rootSet = set(range(1, n + 1))
#         res = 0
#
#         for x, y in pairs3:
#             root1 = find(roots, x)
#             root2 = find(roots, y)
#
#             if root1 != root2:
#                 roots[root2] = root1
#                 rootSet.remove(root2)
#             else:
#                 # 如果 root1 和 root2 一直，说明当前的 (x,y) 这条边的多余的
#                 res += 1
#
#         # 复制 rootSet，剩下的 root 是还没连到图中的。要让 Alice 和 Bob 能走到任意节点，
#         # 那么最后 root1Set 和 root2Set 一定只能剩下一个根节点
#         root1Set = set(rootSet)
#         root2Set = set(rootSet)
#         roots1 = list(roots)
#         roots2 = list(roots)
#
#         # 连接 pairs1 中的节点
#         for x, y in pairs1:
#             root1 = find(roots1, x)
#             root2 = find(roots1, y)
#
#             if root1 != root2:
#                 roots1[root2] = root1
#                 root1Set.remove(root2)
#             else:
#                 res += 1
#
#         # 连接 pairs2 中的节点
#         for x, y in pairs2:
#             root1 = find(roots2, x)
#             root2 = find(roots2, y)
#
#             if root1 != root2:
#                 roots2[root2] = root1
#                 root2Set.remove(root2)
#             else:
#                 res += 1
#
#         if len(root1Set) != 1 or len(root2Set) != 1: return -1
#         return res


# Union Find (简化版本)
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 连接成功返回 True，否则返回 False
        def union(roots, size, x, y):
            root1 = find(roots, x)
            root2 = find(roots, y)
            if root1 != root2:
                # union by rank
                if size[root1] > size[root2]:
                    roots[root2] = root1
                    size[root1] += size[root2]
                else:
                    roots[root1] = root2
                    size[root2] += size[root1]
                return True
            else:
                return False

        # 找 x 的根节点，并把 x 连到根节点上
        def find(roots, x):
            if x != roots[x]:
                # compress
                roots[x] = find(roots, roots[x])
            return roots[x]

        roots1 = list(range(n + 1))
        roots2 = list(range(n + 1))
        size1 = [1 for i in range(n + 1)]
        size2 = [1 for i in range(n + 1)]
        v1 = 0  # Alice 的图中表示成功连接的次数
        v2 = 0  # Bob 的图中表示成功连接的次数
        res = 0
        # 让 type3 排在前面，优先连 type3
        edges.sort(key=lambda x: -x[0])

        for type, x, y in edges:
            if type == 3:
                if union(roots1, size1, x, y) and union(roots2, size2, x, y):
                    v1 += 1
                    v2 += 1
                else:
                    res += 1
            elif type == 1:
                if union(roots1, size1, x, y):
                    v1 += 1
                else:
                    res += 1
            else:
                if union(roots2, size2, x, y):
                    v2 += 1
                else:
                    res += 1

        # 只有 v1 和 v2 都等于 n - 1 时才表明 Alice 和 Bob 能走到所有节点
        return res if v1 == n - 1 and v2 == n - 1 else -1




