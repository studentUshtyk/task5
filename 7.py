class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 1  

            left = dfs(node.left)  
            right = dfs(node.right)  

            
            if left == 0 or right == 0:
                self.camera_count += 1
                return 2

            if left == 2 or right == 2:
                return 1

            return 0

        self.camera_count = 0
        if dfs(root) == 0:  
            self.camera_count += 1

        return self.camera_count
root = TreeNode(0)
root.left = TreeNode(0)
root.left.right = TreeNode(0)

solution = Solution()
print(solution.minCameraCover(root))  # Output: 1
root = TreeNode(0)
root.left = TreeNode(0)
root.left.right = TreeNode(0)
root.left.right.left = TreeNode(0)

solution = Solution()
print(solution.minCameraCover(root))  # Output: 2
