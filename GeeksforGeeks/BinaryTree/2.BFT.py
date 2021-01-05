# BFT or Level Order Traversal
# Method 1 (Use function to print a given level)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def printLevelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        printGivenLevel(root,i)

def printGivenLevel(root,level):
    if root is None:
        return
    if level == 1:
        print(root.data,end=" ")
    elif level > 1:
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1)

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level Order Traversal: ")
    printLevelOrder(root)


# TC = O(n*2) in worst case
# SC = O(n) in worst case
