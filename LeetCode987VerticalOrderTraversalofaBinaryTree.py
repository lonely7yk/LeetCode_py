"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.


Example 1:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:

Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 
Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""

from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # 把所有节点遍历一遍加入到一个 list 中，然后对 list 排序，最后根据 x 坐标加入到不同的组，并把组加入到结果 list
# class Solution:
#     def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
#         # 前序遍历添加所有节点
#         def dfs(node, currX, currY, posList):
#             if not node: return
            
#             posList.append((currX, currY, node.val))
#             dfs(node.left, currX - 1, currY - 1, posList)
#             dfs(node.right, currX + 1, currY - 1, posList)
            
#         posList = []    # 存储 (xPos, yPos, node.val)
#         dfs(root, 0, 0, posList)
#         # 按照 X 升序，Y 降序，val 升序排序
#         posList.sort(key=lambda x: (x[0], -x[1], x[2]))
        
#         xPos = posList[0][0]    # 当前 group 的 x 坐标
#         group = [posList[0][2]] # group 中的 node 值
#         res = []
#         for i in range(1, len(posList)):
#             if posList[i][0] != xPos:
#                 res.append(group)
#                 group = [posList[i][2]]
#                 xPos = posList[i][0]
#             else:
#                 group.append(posList[i][2])
        
#         res.append(group)
#         return res

# BFS + HashMap
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dq = collections.deque()
        dq.append((root, 0))
        resMap = collections.defaultdict(list)

        while dq:
            # 当前层的大小
            size = len(dq)
            # 用于记录当前层的所有位置(x位置)的 node.val
            tmpMap = collections.defaultdict(list)

            for i in range(size):
                node, xPos = dq.popleft()
                tmpMap[xPos].append(node.val)

                if node.left: dq.append((node.left, xPos - 1))
                if node.right: dq.append((node.right, xPos + 1))

            # 当前层的 node.val 添加到对应的 list 之后，对每个 list 进行一次排序
            for xPos in tmpMap:
                # 当前层，同一位置，val 小的排前面
                tmpMap[xPos].sort()
                resMap[xPos].extend(tmpMap[xPos])

        # 对 keys 排序，使 xPos 小的 list 排在前面
        return [resMap[xPos] for xPos in sorted(resMap.keys())]


