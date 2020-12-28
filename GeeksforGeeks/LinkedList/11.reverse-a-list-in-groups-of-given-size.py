class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self,head, k):
        current = head
        prev = None
        next = None
        count = 0

        while(current != None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if (next != None):
            head.next = self.reverse(next, k)

        # new head is prev    
        return prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__=="__main__":
    llist = LinkedList()

    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("before reverse: ")
    llist.printlist()

    print("after reverse: ")
    llist.head = llist.reverse(llist.head, 3)
    llist.printlist()
