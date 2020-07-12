"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge 
list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a 
probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to 
go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it 
differs from the correct answer by at most 1e-5.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of 
success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
 
Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""

# Dijkstra + Heap: O(nlogk)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        visited = {start}   # 表示节点是否加入
        probs = [0 for i in range(n)]   # 表示 start 到每个节点的最大概率
        probs[start] = 1    
        last = start        # 表示上次加入到 visited 的节点
        graph = collections.defaultdict(list)

        # 用邻接表形式保存图
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        # 用于保存每个节点和其对应的概率
        heap = []

        # dijkstra 最多进行 n 次遍历
        for i in range(n):
            # 对于上次添加的节点 last，找他所有的邻接节点，然后更新所有邻接节点，并加入到 heap 中
            for neighbor, p in graph[last]:
                if neighbor in visited: continue
                # 如果更新后概率大于原来，则加入到 heap 中
                if probs[last] * p > probs[neighbor]:
                    probs[neighbor] = probs[last] * p
                    heapq.heappush(heap, (-probs[neighbor], neighbor))  # -probs[neighbor] 用来表示最大堆

            while True:
                # 如果 heap 为空，说明没有可以加入到 visited 的节点了，而且此时也没遍历到 end，所以返回 0
                if not heap: return 0
                # 取出 heap 中的最大概率的邻接节点，如果节点不在 visited 中，则加入到 visited，并把 last 更新为该结点
                (p, idx) = heapq.heappop(heap)
                if idx in visited: continue
                visited.add(idx)
                last = idx
                break

            # 如果加入的节点就是 end，那么直接返回即可
            if last == end:
                return probs[end]

        return 0
