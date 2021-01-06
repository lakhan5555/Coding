''' stack based iterative solution that works in O(n) time '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class BST:
    def constructTree(self,pre,size):
        root = Node(pre[0])
        s = []

        s.append(root)
        i = 0
        while i < size:
            temp = None

            while len(s) > 0 and pre[i] > s[-1].data:
                temp = s.pop()

            if temp != None:
                temp.right = Node(pre[i])
                s.append(temp.right)
            else:
                temp = s[-1]
                temp.left = Node(pre[i])
                s.append(temp.left)

            i += 1
        return root

    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.data,end=" ")
            self.inOrder(root.right)

if __name__=="__main__":
    pre = [10,5,1,7,40,50]
    tree = BST()
    size = len(pre)
    root = tree.constructTree(pre,size)

    print("inOrder: ")
    tree.inOrder(root)
