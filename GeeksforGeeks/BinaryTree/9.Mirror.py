# Convert a Binary Tree into its Mirror Tree

''' Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T)
with left and right children of all non-leaf nodes interchanged '''

# Method 1 - Recursive

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def Mirror(node):
    if node is None:
        return
    else:
        Mirror(node.left)
        Mirror(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)

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
                              
