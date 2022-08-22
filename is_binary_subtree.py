class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return root1.val == root2.val and is_identical(root1.left, root2.left) and is_identical(root2.right, root1.right)


def is_binary_subtree(T, S):
    if S is None:
        return True
    if T is None:
        return False

    if is_identical(T, S):
        return True

    return is_binary_subtree(T.left, S) or is_binary_subtree(T.right, S)


if __name__ == "__main__":
    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)

    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)

    if is_binary_subtree(T, S):
        print("Tree 2 is subtree of Tree 1")
    else:
        print("Tree 2 is not a subtree of Tree 1")

