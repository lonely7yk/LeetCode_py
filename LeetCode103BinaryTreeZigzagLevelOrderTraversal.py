
from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        leftToRight = True
        dq = collections.deque()
        dq.append(root)
        res = []
        
        while dq:
            size = len(dq)
            
            level = []
            for i in range(size):
                node = None
                node = dq.popleft()
                level.append(node.val)
                
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
                    
            if leftToRight:
                res.append(level)
            else:
                res.append(level[::-1])
            leftToRight = not leftToRight
            print(leftToRight)
            
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
res = Solution().zigzagLevelOrder(root)
print(res)
