class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new key
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    # Search for a key
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # Inorder Traversal (Left → Root → Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Preorder Traversal (Root → Left → Right)
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal (Left → Right → Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # Find minimum value node
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Delete a node
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: Get inorder successor
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root


# 🔹 Example Usage
bst = BinarySearchTree()
root = None
nums = [50, 30, 70, 20, 40, 60, 80]

for num in nums:
    root = bst.insert(root, num)

print("Inorder Traversal:", end=" ")
bst.inorder(root)
print("\nPreorder Traversal:", end=" ")
bst.preorder(root)
print("\nPostorder Traversal:", end=" ")
bst.postorder(root)

# Search
print("\n\nSearch for 60:", "Found" if bst.search(root, 60) else "Not Found")

# Delete
print("\nDelete 20")
root = bst.delete(root, 20)
print("Inorder Traversal after deletion:", end=" ")
bst.inorder(root)
