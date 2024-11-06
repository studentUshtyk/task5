class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    count = 0
    result = None

    def inOrderTraversal(node):
        nonlocal count, result
        if not node or result is not None:
            return
        inOrderTraversal(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        inOrderTraversal(node.right)

    inOrderTraversal(root)
    return result
# Приклад 1
root = TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4))
print(kthSmallest(root, 1))  # Output: 1

# Приклад 2
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(kthSmallest(root, 3))  # Output: 3
