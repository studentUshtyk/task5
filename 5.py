class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Серіалізація дерева в рядок"""
        def dfs(node):
            if not node:
                return "null,"
            return str(node.val) + "," + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
    
    def deserialize(self, data: str) -> TreeNode:
        """Десеріалізація дерева з рядка"""
        values = data.split(",")
        self.index = 0
        
        def dfs():
            if values[self.index] == "null":
                self.index += 1
                return None
            node = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

# Приклад використання:
codec = Codec()

# Створення дерева
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Серіалізація
serialized_tree = codec.serialize(root)
print("Serialized:", serialized_tree)

# Десеріалізація
deserialized_tree = codec.deserialize(serialized_tree)
print("Deserialized:", codec.serialize(deserialized_tree))  # Повертає серіалізований рядок для перевірки
# Створення дерева
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Серіалізація
serialized_tree = codec.serialize(root)
print("Serialized:", serialized_tree)  # Output: "1,2,4,null,null,5,null,null,3,null,null,"

# Десеріалізація
deserialized_tree = codec.deserialize(serialized_tree)
print("Deserialized:", codec.serialize(deserialized_tree))  # Output: "1,2,4,null,null,5,null,null,3,null,null,"

