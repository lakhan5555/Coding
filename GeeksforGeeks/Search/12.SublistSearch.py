# Search a linked list in another list
# Given two linked lists, the task is to check whether the
# first list is present in 2nd list or not.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findLinkedList(first,second):

    if not first and not second:
        return False
    if not first or not second:
        return False

    ptr1 = first
    ptr2 = second

    while ptr2:
        ptr2 = second
        while ptr1:
            if not ptr2:
                return False
            elif ptr1.data == ptr2.data:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            else:
                break

        if not ptr1:
            return True

        second = second.next
        ptr1 = first

    return False

node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)

node_b = Node(1)
node_b.next = Node(2)
node_b.next.next = Node(1)
node_b.next.next.next = Node(2)
node_b.next.next.next.next = Node(3)
node_b.next.next.next.next.next = Node(4)

if findLinkedList(node_a,node_b):
    print("List Found")
else:
    print("List Not Found")
