"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. 
If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

Example 1:

Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tile of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)

Sum of every tilt : 0 + 0 + 1 = 1

Example 2:

Input: root = [4,2,9,3,5,null,7]
Output: 15
Explanation: 
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 5 : |0-0| = 0 (no children)
Tilt of node 7 : |0-0| = 0 (no children)
Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15

Example 3:

Input: root = [21,7,14,1,1,2,2,3,3]
Output: 9
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # Two Pass DFS
# class Solution:
#     def findTilt(self, root: TreeNode) -> int:
#         memo = dict()
#         memo[None] = 0
        
#         # 计算 node 下面的所有 sum
#         def calcSum(node):
#             if not node: return 0
            
#             left = calcSum(node.left) if node.left else 0
#             right = calcSum(node.right) if node.right else 0
            
#             memo[node] = left + right + node.val
#             return memo[node]
        
#         # 计算 node 西面所有 tilt 的 sum
#         def dfs(node):
#             if not node: return 0
            
#             left = dfs(node.left) if node.left else 0
#             right = dfs(node.right) if node.right else 0
            
#             return left + right + abs(memo[node.left] - memo[node.right])
        
#         calcSum(root)
#         return dfs(root)


# One Pass DFS
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        memo = dict()
        memo[None] = 0
        
        def calcSum(node):
            if not node: return 0
            
            left = calcSum(node.left) if node.left else 0
            right = calcSum(node.right) if node.right else 0
            
            memo[node] = abs(left - right)
            return left + right + node.val
        
        calcSum(root)
        return sum(memo.values())    

        