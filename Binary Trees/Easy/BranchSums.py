# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def helper(root, branchSums, sum):
    if root is None:
        return
    sum += root.value
    # iterate till leaf node is reached
    if root.left is None and root.right is None:
        branchSums.append(sum)

    helper(root.left, branchSums, sum)
    helper(root.right, branchSums, sum)
    
def branchSums(root):
    branchSums = []
    helper(root, branchSums, 0)
    return branchSums