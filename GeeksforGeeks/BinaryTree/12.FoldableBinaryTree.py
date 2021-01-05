''' Method 2 (Check if Left and Right subtrees are Mirror) '''


class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def isFoldable(root):
    if root is None:
        return True
    return isFoldableUtil(root.left,root.right)

def isFoldableUtil(nodeA,nodeB):
    if nodeA is None and nodeB is None:
        return True
    if nodeA is None or nodeB is None:
        return False
    return isFoldableUtil(nodeA.left,nodeB.right) and isFoldableUtil(nodeA.right,nodeB.left)

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.left.right = Node(5)

    if isFoldable(root):
        print("YES")
    else:
        print("NO")
