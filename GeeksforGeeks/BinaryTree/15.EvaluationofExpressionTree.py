''' Given a simple expression tree, consisting of basic
binary operators i.e., + , – ,* and / and some integers,
 evaluate the expression tree '''

class Node:
     def __init__(self,data):
         self.data = data
         self.left = self.right = None

def Evaluate(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.data)
    left_sum = Evaluate(root.left)
    right_sum = Evaluate(root.right)

    if root.data ==  '+':
        return left_sum + right_sum
    if root.data == '-':
        return left_sum - right_sum
    if root.data == '*':
        return left_sum*right_sum
    else:
        return left_sum/right_sum

if __name__=="__main__":
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node('5')
    root.left.right = Node('4')
    root.right = Node('-')
    root.right.left = Node('100')
    root.right.right = Node('20')

    print("Evaluation of given expression tree: ")
    print(Evaluate(root))

    # another example

    root = Node('+')
    root.left = Node('*')
    root.left.left = Node('5')
    root.left.right = Node('4')
    root.right = Node('-')
    root.right.left = Node('100')
    root.right.right = Node('/')
    root.right.right.left = Node('20')
    root.right.right.right = Node('2')

    print("Evaluation of given expression tree: ")
    print(Evaluate(root))
