''' Question: Given a binary tree, find out if the tree can be
 folded or not '''

''' A tree can be folded if left and right subtrees of the tree are structure
wise mirror image of each other. An empty tree is considered as foldable.'''


''' Method 1 (Change Left subtree to its Mirror
 and compare it with Right subtree) '''


class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def foldable(root):
    if root is None:
        return True

    Mirror(root.left)
    res = isStructSame(root.left,root.right)

    Mirror(root.left)
    return res

def isStructSame(nodeA,nodeB):
    if nodeA is None and nodeB is None:
        return True
    if nodeA != None and nodeB != None and isStructSame(nodeA.left,nodeB.left) and isStructSame(nodeA.right,nodeB.right):
        return True
    return False

def Mirror(node):
    if node is None:
        return
    else:
        Mirror(node.left)
        Mirror(node.right)

        node.left,node.right = node.right,node.left

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.left.right = Node(5)

    if foldable(root):
        print("YES")
    else:
        print("NO")


# TC = O(n)
