"""
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:

Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

Example 3:

Input: grid = [[1,1],[1,1]]
Output: [[1,1]]
Example 4:

Input: grid = [[0]]
Output: [[1,0]]
Example 5:

Input: grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
Output: [[0,1],[1,1],[1,0],[1,0],[1,1]]
 

Constraints:

n == grid.length == grid[i].length
n == 2^x where 0 <= x <= 6
"""

from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# DFS1: 91%
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def constructDFS(grid, left, right, up, down):
            # print(left, right, up, down)
            if left == right: return Node(grid[up][left], True, None, None, None, None)
            
            flag = -1       # 如果循环过后是 0 表示全 0，是 1 表示全 1，是 -1 表示不全一样
            found = False   # 是否已经找到不同的值，用于 break 外层循环
            for i in range(up, down + 1):
                for j in range(left, right + 1):
                    if grid[i][j] == 0:
                        if flag == -1 or flag == 0:
                            flag = 0
                        else:
                            flag = -1
                            found = True
                            break
                    elif grid[i][j] == 1:
                        if flag == -1 or flag == 1:
                            flag = 1
                        else:
                            flag = -1
                            found = True
                            break

                if found: break
                            
            # 如果全一样直接返回
            if flag == 0: return Node(0, True, None, None, None, None)
            elif flag == 1: return Node(1, True, None, None, None, None)
                        
            # 不全一样，用 DFS 构造 4 个子树，然后返回
            midHor = (left + right) // 2
            midVer = (up + down) // 2
        
            topLeft = constructDFS(grid, left, midHor, up, midVer)
            topRight = constructDFS(grid, midHor + 1, right, up, midVer)
            bottomLeft = constructDFS(grid, left, midHor, midVer + 1, down)
            bottomRight = constructDFS(grid, midHor + 1, right, midVer + 1, down)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return constructDFS(grid, 0, len(grid[0]) - 1, 0, len(grid) - 1)
       

# DFS2: 47% 
# class Solution:
#     def construct(self, grid: List[List[int]]) -> 'Node':
#         def constructDFS(grid, x, y, length):
#             if length == 1: return Node(grid[x][y], True, None, None, None, None)

#             topLeft = constructDFS(grid, x, y, length // 2)
#             topRight = constructDFS(grid, x, y + length // 2, length // 2)
#             bottomLeft = constructDFS(grid, x + length // 2, y, length // 2)
#             bottomRight = constructDFS(grid, x + length // 2, y + length // 2, length // 2)

#             if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf \
#                 and topLeft.val == topRight.val and topLeft.val == bottomLeft.val and topLeft.val == bottomRight.val:
#                 return Node(topLeft.val, True, None, None, None, None)
#             else:
#                 return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

#         length = len(grid)
#         return constructDFS(grid, 0, 0, length)


grid = [
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0]
]
res = Solution().construct(grid)
print(res)

