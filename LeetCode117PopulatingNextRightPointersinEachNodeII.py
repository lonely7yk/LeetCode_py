"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next 
pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for 
this problem.
 

Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to 
point to its next right node, just like in Figure B. The serialized output is in level order as connected 
by the next pointers, with '#' signifying the end of each level.
 
Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# follow up: O(1) memory
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        
        leftmost = root
        while leftmost:
            p = leftmost
            first = None    # 表示下一层的第一个元素
            pre = None
            cur = None
            
            while p:
                if p.left:
                    if not pre:
                        pre = p.left
                        first = pre
                    else:
                        # 每遇到一个 node，把上一个 node 连上这个 node，然后更新 pre 为当前 node
                        cur = p.left
                        pre.next = cur
                        pre = cur
                        
                if p.right:
                    if not pre:
                        pre = p.right
                        first = pre
                    else:
                        # 每遇到一个 node，把上一个 node 连上这个 node，然后更新 pre 为当前 node
                        cur = p.right
                        pre.next = cur
                        pre = cur
                        
                p = p.next
            
            leftmost = first
                
        return root        
