''' Method 2 - using BFT (Iterative) '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)

def Mirror(root):
    if root is None:
        return

    q = []
    q.append(root)

    while len(q):
        temp = q.pop(0)

        temp.left, temp.right = temp.right, temp.left

        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("inOrder: ")
    inOrder(root)
    print()

    Mirror(root)
    print("inOrder of Mirror tree: ")
    inOrder(root)
