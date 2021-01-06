class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def getPreIndex():
    return constructTreeUtil.preIndex

def incrementPreIndex():
    constructTreeUtil.preIndex += 1

def constructTreeUtil(pre,low,high,size):
    if (getPreIndex() >= size or low > high):
        return None

    root = Node(pre[getPreIndex()])
    incrementPreIndex()

    if low == high:
        return root
    for i in range(low,high+1):
        if pre[i] > root.data:
            break

    root.left = constructTreeUtil(pre,getPreIndex(),i-1,size)
    root.right = constructTreeUtil(pre,i,high,size)
    return root

def constructTree(pre):
    size = len(pre)
    constructTreeUtil.preIndex = 0
    return constructTreeUtil(pre,0,size-1,size)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

if __name__=="__main__":
    pre = [10,5,1,7,40,50]
    root = constructTree(pre)
    print("inOrder: ")
    inOrder(root)

''' TC = O(n*2) '''                                                 
