"""
Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree 
is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example 1:

Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. 
This is the only good pair.

Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the 
length of ther shortest path between them is 4.

Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Example 4:

Input: root = [100], distance = 1
Output: 0

Example 5:

Input: root = [1,1,1], distance = 2
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 2^10].
Each node's value is between [1, 100].
1 <= distance <= 10
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # DFS: 对于每一个节点，找他的左节点下所有叶子节点高度和右节点下所有叶子节点高度。对于所有叶子节点的高度，
# # 如果左叶子节点的高度+右叶子节点的高度<=distance，就把 cnt 加 1。（这是叶子节点在左右边的情况）
# # 然后还要加上叶子节点在同一边的情况
# # 但这个会多次计算节点高度，时间复杂度高
# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#         def findAllLeafsHeight(node, currHeight, heights):
#             if not node: return []

#             if not node.left and not node.right:
#                 heights.append(currHeight)
#                 return

#             findAllLeafsHeight(node.left, currHeight + 1, heights)
#             findAllLeafsHeight(node.right, currHeight + 1, heights)

#         def dfs(node, distance):
#             if not node: return 0

#             cnt = 0
#             leftHeights = []
#             rightHeights = []
#             findAllLeafsHeight(node.left, 1, leftHeights)
#             findAllLeafsHeight(node.right, 1, rightHeights)

#             leftHeights.sort()
#             rightHeights.sort()

#             for leftHeight in leftHeights:
#                 if leftHeight >= distance: break

#                 for rightHeight in rightHeights:
#                     if leftHeight + rightHeight <= distance:
#                         cnt += 1
#                     else:
#                         break

#             return cnt + dfs(node.left, distance) + dfs(node.right, distance)

#         return dfs(root, distance)

# 需要使用一个全局变量来保存结果
class Solution:
    def __init__(self):
        self.res = 0
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # 返回当前结点的所有子节点高度（小于 distance）
        def dfs(node, distance):
            if not node: return []  # 节点为 null，返回空数组
            if not node.left and not node.right: return [1] # 节点为叶子节点，那么对于上一层来说，该叶子节点高度为 1
            
            # 左叶子节点高度和右叶子节点高度
            leftHeights = dfs(node.left, distance)
            rightHeights = dfs(node.right, distance)
            
            # 找到所有 左高度+右高度<=distance 的组合个数
            self.res += sum([l + r <= distance for l in leftHeights for r in rightHeights])
                        
            # 对于上一层，高度要 + 1
            return [n + 1 for n in leftHeights + rightHeights if n + 1 < distance]
        
        dfs(root, distance)
        return self.res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


distance = 3
res = Solution().countPairs(root, distance)
print(res)
