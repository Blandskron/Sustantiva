class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            print(f"Insertar {key} a la derecha de {root.val}")
            root.right = insert(root.right, key)
        else:
            print(f"Insertar {key} a la izquierda de {root.val}")
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Ejemplo de uso
root = TreeNode(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Recorrido Inorder del árbol:")
inorder_traversal(root)

