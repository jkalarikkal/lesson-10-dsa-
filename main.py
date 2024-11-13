class Treenode:
    def __init__(self, h):
        self.data = h
        self.left = None
        self.right = None
    

def Inorder(root): #ldr
    if root is not None:
        if root.left is not None:
            Inorder(root.left)
        print(root.data)
        if root.right is not None:
            Inorder(root.right)

def Inserty(root, x):
    if root == None:
        return Treenode(x)
    if root.data > x:
        root.left = Inserty(root.left, x)
    else:
        root.right = Inserty(root.right, x)
    
    return root

def Search(root, z):
    if root.data == z:
        return root
    elif root.data > z and root.left is not None:
        return Search(root.left, z)
    elif root.data < z and root.right is not None:
        return Search(root.right, z)

    else:
        return -1

quest = int(input("How many elements do you want in your tree? "))

root = None


for i in range (quest):
    num = int(input("What number do you want: "))
    root = Inserty(root, num)

Inorder(root)

inny = int(input("What number would you like to search for? "))

key = Search(root, inny)

if key == -1:
    print("number does not exist within the tree")
else:
    print("Your number does exist within the tree")