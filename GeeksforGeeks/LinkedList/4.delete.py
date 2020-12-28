# delete a node after a given key

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

    def delete(self,key):

        temp = self.head

        # if head has key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key is not present
        if temp == None:
            return

        prev.next = temp.next
        temp = None

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

    print("LinkedList: ")
    llist.printlist()

    llist.delete(1)
    print("after deletion of 1: ")
    llist.printlist()
