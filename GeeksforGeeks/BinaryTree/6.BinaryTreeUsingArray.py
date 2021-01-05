tree = [None]*10

def root(key):
    if tree[0] is not None:
        print("Root already exist!")
    else:
        tree[0] = key

def set_left(key,parent):
    if tree[parent] is None:
        print("Child can't set at",2*parent + 1,"no parent found")
    else:
        tree[2*parent + 1] = key

def set_right(key,parent):
    if tree[parent] is None:
        print("Child can't set at", 2*parent+2,"no parent found")
    else:
        tree[2*parent + 2] = key

def printTree():
    for i in range(10):
        if tree[i] is not None:
            print(tree[i],end=" ")
        else:
            print("-",end=" ")
    print()

root('A')
set_right('C',0)
set_left('D',1)
set_right('E',1)
set_right('F',2)

printTree()                        
