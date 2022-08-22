
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, value):
        if self.val:
            if value < self.val:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.val:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.val = value

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()

    def search(self, root, key):
        if root is None or root.val == key:
            return root

        if root.val < key:
            if root.right is None:
                return str(key) + " Not Found"
            return self.search(root.right, key)
        if self.left is None:
            return str(key) + " Not Found"
        return self.search(root.left, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def min_val_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None or root.val == key:








if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    # print(root.val)
    root.inorder(root)
    print(root.search(root, 7))
    # root.print_tree()