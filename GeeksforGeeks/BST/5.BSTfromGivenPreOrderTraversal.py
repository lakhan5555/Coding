''' Method 2 ( O(n) time complexity ) '''

INT_MIN = float("-inf")
INT_MAX = float("inf")

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def getPreIndex():
    return constructTreeUtil.preIndex

def incrementPreIndex():
    constructTreeUtil.preIndex += 1

def constructTreeUtil(pre,key,mini,maxi,size):
    if getPreIndex() >= size:
        return None

    root = None

    if (key > mini and key < maxi):
        root = Node(key)
        incrementPreIndex()

        if getPreIndex() < size:
            root.left = constructTreeUtil(pre,pre[getPreIndex()],mini,key,size)
        if getPreIndex() < size:
            root.right = constructTreeUtil(pre,pre[getPreIndex()],key,maxi,size)
    return root

def constructTree(pre):
    size = len(pre)
    constructTreeUtil.preIndex = 0
    return constructTreeUtil(pre,pre[0],INT_MIN,INT_MAX,size)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

if __name__=="__main__":
    pre = [10,5,1,7,40,50]
    root = constructTree(pre)
    print("inOrder: ")
    inOrder(root)
