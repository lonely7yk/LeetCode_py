from typing import List
import collections


class Solution:
    # BFS: 92ms 50%
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        dq = collections.deque()
        graph = [[] for i in range(n + 1)]  # 邻接表
        visited = [False for i in range(n + 1)]  # 某节点是否访问
        visited[1] = True
        probs = [0 for i in range(n + 1)]  # 走到某个节点的概率
        probs[1] = 1
        cnt = 0  # 记录现在走了多少步
        dq.append(1)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        while dq:
            if cnt == t: break

            size = len(dq)
            for i in range(size):
                idx = dq.popleft()
                prob = probs[idx]

                # 计算当前结点周围还有多少节点可以走
                num = len(graph[idx])
                if idx != 1:
                    num -= 1

                if num == 0: continue

                for j in graph[idx]:
                    if visited[j]: continue

                    visited[j] = True
                    dq.append(j)
                    probs[j] = prob / num

                if num > 0: probs[idx] = 0
            cnt += 1

        return probs[target]