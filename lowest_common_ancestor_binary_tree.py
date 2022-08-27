# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, value):
        if self.val:
            if value < self.val:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            elif value > self.val:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
        else:
            self.val = value

class Solution:
    def findPath(self, root, path, k):
        if root is None:
            return False

        path.append(root.val)
        if k.val == root.val:
            return True
        if (root.left != None and self.findPath(root.left, path, k)) or (
                root.right != None and self.findPath(root.right, path, k)):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        p_track = self.findPath(root=root, path=path1, k=p)
        q_track = self.findPath(root=root, path=path2, k=q)
        if not (p_track or q_track):
            return -1
        i = 0
        while (i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        res = TreeNode(path1[i - 1])
        return res

if __name__ == "__main__":
    root = TreeNode(6)
    root.insert(2)
    root.insert(8)
    root.insert(0)
    root.insert(4)
    root.insert(7)
    root.insert(9)