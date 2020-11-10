"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, 
and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]

Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # 用一个数组存放所有 node（从索引为 1 开始存），那么子节点索引为 n，其父节点一定为 n // 2
# class CBTInserter:
#     def __init__(self, root: TreeNode):
#         self.array = [None] # array[0] 不存 node
#         dq = collections.deque([root])
#         # 先用 BFS 把所有节点存进 array
#         while dq:
#             node = dq.popleft()
#             self.array.append(node)
#             if node.left: dq.append(node.left)
#             if node.right: dq.append(node.right)
                

#     def insert(self, v: int) -> int:
#         node = TreeNode(v)
#         n = len(self.array)
#         parentNode = self.array[n // 2]
        
#         # 需要判断 parentNode 是否存在
#         if n % 2 == 0:
#             parentNode.left = node
#         else:
#             parentNode.right = node
#         self.array.append(node)
#         return parentNode.val
        

#     def get_root(self) -> TreeNode:
#         return self.array[1]


# Use Deque to store nodes that don't have both left and right children.
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.dq = collections.deque()
        self.root = root
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.dq.append(node)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            

    def insert(self, v: int) -> int:
        node = self.dq[0]
        newNode = TreeNode(v)
        if not node.left:
            node.left = newNode
        else:
            node.right = newNode
            self.dq.popleft()
        self.dq.append(newNode)
        return node.val
        

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
