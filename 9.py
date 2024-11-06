class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        stack = []
        i = 0
        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(value)
            
            if depth == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                while len(stack) > depth:
                    stack.pop()
                stack[-1].right = node

            stack.append(node)
        
        return stack[0]

    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result

traversal = "1-2--3--4-5--6--7"
solution = Solution()
root = solution.recoverFromPreorder(traversal)
print(solution.levelOrder(root))  # Виведення дерева в порядку рівнів
