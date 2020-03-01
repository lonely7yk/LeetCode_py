import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS: 120ms 50%
# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         res = ""
#         queue = collections.deque()
#         queue.append(root)
        
#         while queue:
#             node = queue.popleft()
#             if node is None:
#                 res += "N#"
#                 continue
            
#             res += str(node.val) + "#"
            
#             queue.append(node.left)
#             queue.append(node.right)
            
#         return res
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         queue = collections.deque()
#         idx = data.find("#")
#         s = data[:idx]
#         if s == "N":
#             return None
        
#         root = TreeNode(int(s))
#         queue.append(root)
#         data = data[idx+1:]
        
#         while queue:
#             node = queue.popleft()
            
#             idx1 = data.find("#")
#             idx2 = data.find("#", idx1 + 1)
#             s1 = data[:idx1]
#             s2 = data[idx1+1:idx2]
            
#             if s1 == "N":
#                 node.left = None
#             else:
#                 tmp = TreeNode(int(s1))
#                 node.left = tmp
#                 queue.append(tmp)
                
#             if s2 == "N":
#                 node.right = None
#             else:
#                 tmp = TreeNode(int(s2))
#                 node.right = tmp
#                 queue.append(tmp)
                
#             data = data[idx2+1:]

#         return root

# DFS: 112ms 87%
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "N#";

        return str(root.val) + "#" + self.serialize(root.left) + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(queue):
            s = queue.popleft()
            if s == "N":
                return None

            node = TreeNode(int(s))
            node.left = dfs(queue)
            node.right = dfs(queue)
            return node

        nodes = data.split("#")[:-1]    # 最后一个是空，去掉
        queue = collections.deque()
        queue.extend(nodes)

        return dfs(queue)

      

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

c = Codec()
s = c.serialize(root)
print(s)
root = c.deserialize(s)
print(c.serialize(root))