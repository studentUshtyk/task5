# Визначення структури бінарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    def isMirror(left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    return isMirror(root.left, root.right) if root else True

# Приклад 1 для перевірки
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(isSymmetric(root))  # Output: True

# Приклад 2
root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(isSymmetric(root))  # Output: False
