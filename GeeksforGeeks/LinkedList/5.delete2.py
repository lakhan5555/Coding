# Delete a Linked List node at a given position

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, position):

        # if linked list is empty
        if self.head == None:
            return

        temp = self.head

        # if head needs to be removed
        if position == 0:
            self.head = temp.head
            temp = None
            return

        # lets store the position of previous node of node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp == None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        a = temp.next.next
        temp.next = None
        temp.next = a

    def printlist(self):
        temp = self.head

        while(temp):
                print(temp.data)
                temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(8)

    print("LinkedList: ")
    llist.printlist()

    llist.delete(4)
    print("LinkedList after deletion at position 4")
    llist.printlist()
