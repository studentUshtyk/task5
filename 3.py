class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
def treeToList(root: TreeNode) -> list:
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

# Приклад 1
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted_root = invertTree(root)
print(treeToList(inverted_root))  # Output: [4, 7, 2, 9, 6, 3, 1]

# Приклад 2
root = TreeNode(2, TreeNode(1), TreeNode(3))
inverted_root = invertTree(root)
print(treeToList(inverted_root))  # Output: [2, 3, 1]

# Приклад 3
root = None
inverted_root = invertTree(root)
print(treeToList(inverted_root))  # Output: []
