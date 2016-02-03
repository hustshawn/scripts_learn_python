# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    # @param root, a tree node
    # @return a list of integers
    def Insert(self, root, x):
        if root == None:
            root = TreeNode(x)
        else:
            if x < root.val:
                root.left = self.Insert(root.left, x)
            if x > root.val:
                root.right = self.Insert(root.right, x)
        return root

    def Delete(self, root, x):
        if root:
            if x < root.val:
                root.left = self.Delete(root.left, x)
            elif x > root.val:
                root.right = self.Delete(root.right, x)
            elif root.left and root.right:
                tmp = self.FindMin(root.right)
                root.val = tmp.val
                root.right = self.Delete(root.right, root.val)
            else:
                tmp = root
                if root.left is None: root = root.right
                elif root.right is None: root = root.left
        return root

    def FindMin(self, root):
        if root:
            while root.left:
                root = root.left
        
        return root

    def preorder(self, root):
        if root:
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)

Tree = BinarySearchTree()
root = None
# l = [6, 2, 8, 1, 5, 3, 4]
l = [2,1,3]
for i in range(len(l)):
    root = Tree.Insert(root, l[i])
Tree.preorder(root)
root = Tree.Delete(root, 2)
Tree.preorder(root)