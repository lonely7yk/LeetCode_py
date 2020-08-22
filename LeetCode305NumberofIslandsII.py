"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""


from typing import List

# Union Find: O(k log mn)
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(roots, pos):
            if pos == roots[pos]:
                return pos
            else:
                roots[pos] = find(roots, roots[pos])    # path compression
                return roots[pos]
                
        # 存储所有节点的父节点，-1 表示当前结点还是海
        roots = [-1 for i in range(m * n)]
        # 表示当前结点下结点个数
        size = [0 for i in range(m * n)]
        cnt = 0
        res = []
        
        for x, y in positions:
            pos = x * n + y
            
            # 重复添加
            if roots[pos] != -1: 
                res.append(res[-1])
                continue
                
            # 先把 root 设成自己
            roots[pos] = pos
            size[pos] += 1
            cnt += 1

            # 遍历周围的点            
            for tmpX, tmpY in ((x+1,y), (x-1,y), (x,y-1), (x,y+1)):
                tmpPos = tmpX * n + tmpY
                if 0 <= tmpX < m and 0 <= tmpY < n and roots[tmpPos] >= 0:
                    # union by rank
                    # 找到邻居节点的 root 和当前结点的 root
                    root1 = find(roots, tmpPos)
                    root2 = find(roots, pos)
                    
                    if root1 != root2:
                        # 把数量少的节点加到数量多的节点上
                        if size[root1] >= size[root2]:
                            roots[root2] = root1
                            size[root1] += size[root2]
                        else:
                            roots[root1] = root2
                            size[root2] += size[root1]
                            
                        cnt -= 1
            
            res.append(cnt)
                    
        return res