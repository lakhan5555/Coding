# insert a key in level order Traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(temp):
    if temp:
        inOrder(temp.left)
        print(temp.data,end=" ")
        inOrder(temp.right)

def Insert(root, key):
    if root is None:
        root = Node(key)
        return
    q = []
    q.append(root)
    while len(q) > 0:
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("InOrder before insertion: ")
    inOrder(root)

    key = 6
    Insert(root,key)
    print()
    print("InOrder after insertion: ")
    inOrder(root)
