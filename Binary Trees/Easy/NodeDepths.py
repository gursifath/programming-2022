def helper(root, depth):
    if root is None:
        return 0

    return depth + helper(root.left, depth+1) + helper(root.right, depth+1)

def nodeDepths(root):
    return helper(root, 0)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
