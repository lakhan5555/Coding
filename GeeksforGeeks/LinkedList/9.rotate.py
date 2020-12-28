# Given a singly linked list, rotate the linked list counter-clockwise
# by k nodes.
#  k is a given positive integer


# method - 1

# To rotate the linked list, we need to change next of kth node to NULL,
# next of the last node to the previous head node, and finally,
# change head to (k+1)th node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def rotate(self, key):
        if key==0:
            return

        curr = self.head
        count = 1

        while (count < key and curr is not None ):
            curr = curr.next
            count += 1

        if curr is None:
            return

        kthNode = curr

        while curr.next != None:
            curr = curr.next

        curr.next = self.head
        self.head = kthNode.next
        kthNode.next = None


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__=="__main__":
    llist = Linkedlist()

    for i in range(60,0,-10):
        llist.push(i)

    print("before rotation: ")
    llist.printList()

    key = 4
    print("after rotation: ")
    llist.rotate(key)
    llist.printList()



# Tc = O(n)
