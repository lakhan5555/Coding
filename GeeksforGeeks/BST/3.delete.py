class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

def insert(node,key):
    if node is None:
        return Node(key)
    else:
        if node.data == key:
            return node
        elif node.data < key:
            node.right = insert(node.right,key)
        else:
            node.left = insert(node.left,key)
    return node

def inOrderSuccessor(node):
    curr = node
    while curr.left != None:
        curr = curr.left
    return curr

def delete(root,key):
    if root is None:
        return root
    if root.data > key:
        root.left = delete(root.left,key)
    elif root.data < key:
        root.right = delete(root.right,key)
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root.right = None
            return temp
        elif root.right is None:
            temp = root.left
            root.left = None
            return temp

        # Node with two children
        temp = inOrderSuccessor(root.right)
        root.data = temp.data

        root.right = delete(root.right,temp.data)

    return root


if __name__ == "__main__":
    root = Node(50)
    insert(root,30)
    insert(root,20)
    insert(root,40)
    insert(root,70)
    insert(root,60)
    insert(root,80)

    print("inOrder traversal: ")
    inOrder(root)
    print()

    print("Delete 20 :")
    delete(root,20)
    print("inOrder traversal: ")
    inOrder(root)
    print()

    print("Delete 30 :")
    delete(root,30)
    print("inOrder traversal: ")
    inOrder(root)
    print()

    print("Delete 50 :")
    delete(root,50)
    print("inOrder traversal: ")
    inOrder(root)
