# method 1 - Iterative Approach

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        curr = self.head

        while curr != None :
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        self.head = prev

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":

    llist = Linkedlist()

    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print("Linkedlist: ")
    llist.printList()

    print("After reverse: ")
    llist.reverse()
    llist.printList()


# TC = O(n)
# SC = O(1)
