# Method 2 - Using BFS (Queue)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isContinuous(root):
    if root is None:
        return False
    q = []
    flag = 1
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.left:
            if abs(temp.left.data - temp.data) == 1:
                q.append(temp.left)
            else:
                flag = 0
                break
        if temp.right:
            if abs(temp.right.data - temp.data) == 1:
                q.append(temp.right)
            else:
                flag = 0
                break

    if flag:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    root = Node(3)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.right = Node(5)

    isContinuous(root)


# TC = O(n)
