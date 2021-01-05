''' Given a binary tree, delete a node from it by making sure that tree shrinks
from the bottom (i.e. the deleted node is replaced by bottom most
and rightmost node) '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(temp):
    if temp is None:
        return
    inOrder(temp.left)
    print(temp.data,end=" ")
    inOrder(temp.right)

def deleteDeepest(root,nodeD):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp is nodeD:
            temp = None
            return
        if temp.right:
            if temp.right is nodeD:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is nodeD:
                temp.left = None
                return
            else:
                q.append(temp.left)

def deletion(root,key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root

    q = []
    node_k = None
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.data == key:
            node_k = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if node_k:
        x = temp.data
        deleteDeepest(root,temp)
        node_k.data = x

    return root

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("InOrder before deletion: ")
    inOrder(root)
    print()

    key = 11
    deletion(root,key)
    print("InOrder after deletion: ")
    inOrder(root)
