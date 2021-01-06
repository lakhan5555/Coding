''' An empty tree is height-balanced.
A non-empty binary tree T is balanced if:
1) Left subtree of T is balanced
2) Right subtree of T is balanced
3) The difference between heights of left subtree
and right subtree is not more than 1 '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right)) + 1

def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh-rh) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True
    return False

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    if isBalanced(root):
        print("Balanced")
    else:
        print("Not Balanced")

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)

    if isBalanced(root):
        print("Balanced")
    else:
        print("Not Balanced")

''' TC = O(n*2)
    see another aproach of O(n) time '''                                        
