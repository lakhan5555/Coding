class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    # inserting at front
    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # inserting after a given Node
    def inserAfter(self,prevNode, new_data):

        if prevNode is None:
            print("Previous node is empty")
            return

        new_node = Node(new_data)
        new_node.next = prevNode.next
        prevNode.next = new_node

    # inserting at end
    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


if __name__=="__main__":
    llist = LinkedList()

    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.inserAfter(llist.head.next, 8)

    llist.printlist()
