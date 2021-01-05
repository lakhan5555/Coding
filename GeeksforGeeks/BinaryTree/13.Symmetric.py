''' check if given binary tree is symmetric or not
i.e is mirror image of itself or not '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def isSymmetric(root):
    return isMirror(root,root)

def isMirror(nodeA, nodeB):
    if nodeA is None and nodeB is None:
        return True
    if nodeA != None and nodeB != None:
        if nodeA.data == nodeB.data:
            return isMirror(nodeA.left,nodeB.right) and isMirror(nodeA.right,nodeB.left)
    return False

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    if isSymmetric(root):
        print("YES")
    else:
        print("NO")                      
