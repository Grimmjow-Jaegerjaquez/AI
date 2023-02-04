class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key
    

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        elif root.val > key:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


r = Node(25)
r = insert(r, 15)
r = insert(r, 50)
r = insert(r, 10)
r = insert(r, 22)
r = insert(r, 35)
r = insert(r, 70)
r = insert(r, 4)
r = insert(r, 12)
r = insert(r, 18)
r = insert(r, 24)
r = insert(r, 31)
r = insert(r, 44)
r = insert(r, 66)
r = insert(r, 90)

print("Inorder Traversal : ")
inorder(r)
print("\n")

print("Preorder Traversal : ")
preorder(r)
print("\n")

print("Postorder Traversal : ")
postorder(r)
print("\n")