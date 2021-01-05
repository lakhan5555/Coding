''' A tree is a Continuous tree if in each root to leaf path,
the absolute difference between keys of two adjacent is 1 '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isContinuous(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left is None:
        return (abs(node.right.data - node.data) == 1) and isContinuous(node.right)
    if node.right is None:
        return (abs(node.left.data - node.data) == 1) and isContinuous(node.left)

    return (abs(node.right.data - node.data) == 1) and (abs(node.left.data - node.data) == 1) and isContinuous(node.right) and isContinuous(node.left)

if __name__=="__main__":
    root = Node(3)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.right = Node(5)

    if isContinuous(root):
        print("Yes")
    else:
        print("No")
