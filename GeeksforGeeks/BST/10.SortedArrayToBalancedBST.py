class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def SortedArrayToBalancedBST(arr) :
    if not arr:
        return None

    mid = int(len(arr)/2)
    root = Node(arr[mid])

    root.left = SortedArrayToBalancedBST(arr[:mid])
    root.right = SortedArrayToBalancedBST(arr[mid+1:])

    return root

def preOrder(node):
    if node:
        print(node.data,end=" ") 
        preOrder(node.left)
        preOrder(node.right)

arr = [1,2,3,4,5,6,7]
root = SortedArrayToBalancedBST(arr)

print("preOrder traversal: ")
preOrder(root)
