from collections import defaultdict
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root:
            return []
        
        column_table = defaultdict(list)
        
        queue = [(root, 0)]
        
        while queue:
            node, column = queue.pop(0)
            
            column_table[column].append(node.val)
            
            if node.left:
                queue.append((node.left, column - 1))
            
            if node.right:
                queue.append((node.right, column + 1))
        
        sorted_columns = sorted(column_table.keys())
        
        return [sorted(column_table[column]) for column in sorted_columns]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.verticalOrder(root))  # Output: [[9], [3, 15], [20], [7]]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.verticalOrder(root))  # Output: [[4], [2], [1, 5, 6], [3], [7]]
