# Method 1(Simply use two loops)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def intersection(self,head1, head2):
        curr1 = head1
        curr2 = head2

        while curr1:
            while curr2:
                if curr1.data == curr2.data:
                    print("found: ")
                    print(curr1.data)
                    break

                curr2 = curr2.next

            curr1 = curr1.next

        print("not found!")


if __name__=="__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.head = Node(10)
    llist2.head = Node(3)

    llist2.head.next = Node(6)
    llist2.head.next.next = Node(9)

    newNode = Node(15)
    llist2.head.next.next.next = newNode
    llist1.head.next =  newNode
    llist1.head.next.next = Node(30)
    llist1.head.next.next.next = None

    llist1.intersection(llist1.head, llist2.head)
