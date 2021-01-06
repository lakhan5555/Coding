class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root,key):
    if root == None or root.data == key:
        return root
    if root.data < key:
        return search(root.right,key)
    else:
        return search(root.left,key)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

if __name__=="__main__":
    root = Node(50)
    insert(root,30)
    insert(root,20)
    insert(root,40)
    insert(root,70)
    insert(root,60)
    insert(root,80)

    key = 40
    s = search(root,key)
    print(s.data)
