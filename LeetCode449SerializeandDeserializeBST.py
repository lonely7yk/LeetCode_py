"""
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection 
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on 
how your serialization/deserialization algorithm should work. You just need to ensure that a binary 
search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize 
algorithms should be stateless.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # 如果为空不需要用一个字符来表示，直接返回空字符串即可
        if root is None: return ''
        
        return str(root.val) + '#' + self.serialize(root.left) + self.serialize(root.right)
            
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def dfs(queue, lb, hb):
            # queue 为空需要返回 None
            if not queue: return None
            peek = int(queue[0])
            # 保证当前结点在正确的子树上
            if peek < lb or peek > hb: return None
            
            val = int(queue.popleft())
            node = TreeNode(val)
            node.left = dfs(queue, lb, val)
            node.right = dfs(queue, val, hb)
            return node
            
        queue = collections.deque(data.split('#')[:-1])
        root = dfs(queue, float('-inf'), float('inf'))
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
