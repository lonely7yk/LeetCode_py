"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

- A solution using O(n) space is pretty straight forward.
- Could you devise a constant space solution?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # # Inorder Traserval:  O(nlogn) - O(n) 72ms 53.5%
    # # mine: 先前序遍历保存在一个 list 中后，排序，然后再做一次前序遍历把数组中的值赋到节点上
    # def recoverTree(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     nodes = []
    #     # nodes = [float('-inf')]

    #     def inOrderTraversal(root, nodes):
    #         """ 将元素加入到 nodes 中 """
    #         if root is not None:
    #             inOrderTraversal(root.left, nodes)
    #             nodes.append(root.val)
    #             inOrderTraversal(root.right, nodes)

    #     inOrderTraversal(root, nodes)
    #     nodes.sort()
    #     # 注释中的方法可把排序的时间复杂度降到 O(n) 但是最终的速度却要 92ms
    #     # nodes.append(float('inf'))
    #     # idx1, idx2 = -1, -1
    #     # for i in range(1, len(nodes) - 1):
    #     #     if nodes[i] > nodes[i - 1] and nodes[i] > nodes[i + 1] and idx1 == -1:
    #     #         idx1 = i
    #     #     if nodes[i] < nodes[i - 1] and nodes[i] < nodes[i + 1]:
    #     #         idx2 = i

    #     # nodes[idx1], nodes[idx2] = nodes[idx2], nodes[idx1]
    #     # # 把 -inf 和 inf 去掉
    #     # nodes.pop(0)
    #     # nodes.pop()


    #     def inOrderTraversal2(root, nodes):
    #         """ 用来赋值 """
    #         if root is not None:
    #             inOrderTraversal2(root.left, nodes)
    #             root.val = nodes.pop(0)
    #             inOrderTraversal2(root.right, nodes)

    #     inOrderTraversal2(root, nodes)

    # Inorder Traserval: O(n) - O(1) 68ms 60.56%
    def __init__(self):
        self.firstNode, self.secondNode = None, None
        self.preNode = TreeNode(float('-inf'))  # 为了在第一次判断时不进行赋值，所以设成 -inf

    def recoverTree(self, root: TreeNode) -> None:
        self.inOrderTraversal(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val


    def inOrderTraversal(self, root):
        if not root: return

        self.inOrderTraversal(root.left)

        # 这两个判断语句很重要，在 firstNode 没赋值的时候，如果 preNode 的值比当前值大，则对 firstNode 赋 preNode
        # 如果 firstNode 赋过值了则不需要继续赋值，因为 secondNode 前一个元素（preNode）也满足这个条件
        if not self.firstNode and self.preNode.val >= root.val:
            self.firstNode = self.preNode

        # 在 firstNode 赋值之后，才会赋 secondNode 的值，因为本来是顺序的，交换两个元素以后，大的元素（firstNode）在
        # 前面，小的元素（secondNode）在后面。另外 firstNode 后面一个元素也满足这个条件，但是因为如果后面还满足条件，会
        # 把当前值覆盖
        if self.firstNode and self.preNode.val >= root.val:
            self.secondNode = root

        self.preNode = root # 当前值判断完后把当前 root 赋给 preNode

        self.inOrderTraversal(root.right)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    Solution().recoverTree(root)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.right.left.val)

    # root = TreeNode(1)
    # root.left = TreeNode(3)
    # root.left.right = TreeNode(2)
    # Solution().recoverTree(root)
    # print(root.val)
    # print(root.left.val)
    # print(root.left.right.val)

    # root = TreeNode(146)
    # root.left = TreeNode(71)
    # root.left.left = TreeNode(55)
    # root.left.left.left = TreeNode(321)
    # root.left.left.left.left = TreeNode(-33)
    # root.right = TreeNode(-13)
    # root.right.left = TreeNode(231)
    # root.right.right = TreeNode(399)
    # Solution().recoverTree(root)