class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        
        

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            
        else:
            self._insert(key)
            
    
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)
                
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key >= node.key:
            self._search(node.right, key)
        else:
            self._search(node.left, key)
            
        
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    
    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])
    
    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result