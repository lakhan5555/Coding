''' The expression tree is a binary tree in which each internal node corresponds
to the operator and each leaf node corresponds to the operand  '''

''' Inorder traversal of expression tree produces
infix version of given postfix expression
(same with postorder traversal it gives prefix expression) '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data,end=" ")
        Inorder(root.right)

def isOperator(x):
    if (x == '+' or x == '-' or x == '*' or x == '/' or x == '^'):
        return True
    else:
        return False

def constructTree(postfix):
    stack = []

    for char in postfix:
        if not isOperator(char):
            t = Node(char)
            stack.append(t)
        else:
            t = Node(char)
            t1 = stack.pop()
            t2 = stack.pop()

            t.right = t1
            t.left = t2

            stack.append(t)
    return stack.pop()

if __name__=="__main__":
    postfix = "ab+ef*g*-"
    r = constructTree(postfix)  
    print("Infix Expression is")
    Inorder(r)
