class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def helper(node):
            if not node:
                return 0  
            
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)  
            
            current_path_sum = node.val + left_gain + right_gain
            
            self.max_sum = max(self.max_sum, current_path_sum)
            
            return node.val + max(left_gain, right_gain)
        
        helper(root)
        return self.max_sum
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

solution = Solution()
print(solution.maxPathSum(root))  # Output: 6
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.maxPathSum(root))  # Output: 42
