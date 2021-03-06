"""
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the 
original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. 
Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is 
no restriction on how your encode/decode algorithm should work. You just need to ensure that an 
N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original 
N-nary tree structure.

Nary-Tree input serialization is represented in their level order traversal, each group of children 
is separated by the null value (See following example).

For example, you may encode the following 3-ary tree to a binary tree in this way:

Input: root = [1,null,3,2,4,null,5,6]
Note that the above is just an example which might or might not work. You do not necessarily need 
to follow this format, so please be creative and come up with different approaches yourself.

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
Do not use class member/global/static variables to store states. Your encode and decode algorithms 
should be stateless.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# # BFS: O(n)
# class Codec:
#     # Encodes an n-ary tree to a binary tree.
#     def encode(self, root: 'Node') -> TreeNode:
#         if not root: return None
        
#         newRoot = TreeNode(root.val)
#         dq = collections.deque([(root, newRoot)])
        
#         while dq:
#             node, treeNode = dq.popleft()
#             dumb = TreeNode(-1)
#             p = dumb
            
#             for child in node.children:
#                 tmp = TreeNode(child.val)
#                 p.right = tmp
#                 p = p.right
#                 dq.append((child, tmp))
                
#             treeNode.left = dumb.right
                
#         return newRoot
        
    
#     # Decodes your binary tree to an n-ary tree.
#     def decode(self, data: TreeNode) -> 'Node':
#         if not data: return None
        
#         root = Node(data.val)
#         dq = collections.deque([(root, data)])
        
#         while dq:
#             node, treeNode = dq.popleft()
            
#             p = treeNode.left
#             children = []
#             while p:
#                 tmp = Node(p.val)
#                 children.append(tmp)
#                 dq.append((tmp, p))
#                 p = p.right
                
#             node.children = children
            
#         return root


# DFS: O(n)
class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        def dfs(node):
            if not node: return None
            
            treeNode = TreeNode(node.val)
            dumb = TreeNode(-1)
            p = dumb
            
            for child in node.children:
                p.right = dfs(child)
                p = p.right
                
            treeNode.left = dumb.right
            return treeNode
        
        return dfs(root)
            
    
    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        def dfs(treeNode):
            if not treeNode: return None
            
            node = Node(treeNode.val)
            p = treeNode.left
            children = []
            
            while p:
                tmp = dfs(p)
                children.append(tmp)
                p = p.right
        
            node.children = children
            return node
        
        return dfs(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
