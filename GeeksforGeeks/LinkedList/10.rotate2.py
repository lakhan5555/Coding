# method - 2

# To rotate a linked list by k, we can first make the linked list circular
# and then moving k-1 steps forward from head node, making it null and
# make kth node as head.

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

        while curr.next != None :
            curr = curr.next

        curr.next = self.head

        curr = self.head
        count = 1
        while count < key:
            curr = curr.next
            count += 1

        self.head = curr.next
        curr.next = None

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
