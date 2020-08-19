import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deserialize(arr):
    valDq = collections.deque(arr)
    root = TreeNode(valDq.popleft())
    nodeDq = collections.deque([root])

    while nodeDq:
        node = nodeDq.popleft()
        if valDq:
            val = valDq.popleft()
            if val is not None: node.left = TreeNode(val)
        if valDq:
            val = valDq.popleft()
            if val is not None: node.right = TreeNode(val)

        if node.left: nodeDq.append(node.left)
        if node.right: nodeDq.append(node.right)

    return root


if __name__ == '__main__':
    arr = [0, 2, 1, None, None, 3]
    root = deserialize(arr)
    print()
