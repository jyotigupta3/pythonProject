
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

    def findPath(self, root, path, k):
        if root is None:
            return path

        if k.val < root.val:
            path.append(root.val)
            self.findPath(root.left, path, k)
        if k.val > root.val:
            path.append(root.val)
            self.findPath(root.right, path, k)

        if k.val == root.val:
            path.append(root.val)
        return path

    def lowestCommonAncestor(self, root, p, q):
        p_track = []
        q_track = []
        p_track = self.findPath(root, p_track, p)
        q_track = self.findPath(root, q_track, q)
        i = 0
        while i < len(p_track) and i < len(q_track):
            if p_track[i] != q_track[i]:
                break

            i += 1
        return p_track[i - 1]


if __name__ == "__main__":
    root = Node(6)
    root.insert(2)
    root.insert(8)
    root.insert(0)
    root.insert(4)
    root.insert(7)
    root.insert(9)
    # root.insert(None)
    # root.insert(None)
    root.insert(3)
    root.insert(5)
    # print(root.val)
    # root.inorder(root)
    # print(root.search(root, 7))
    p = Node(2)
    q = Node(8)
    print(root.lowestCommonAncestor(root, p, q))
    # root.print_tree()