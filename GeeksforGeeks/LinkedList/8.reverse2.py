# method 2 - Recursive Approach

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

    def reverse(self, head):

        # if head is null or reached the list end
        if head is None or head.next is None:
            return head

        rest = self.reverse(head.next)

        head.next.next = head
        head.next = None

        return rest

    # returns the Linkedlist in display format

    def __str__(self):
        LinkedlistStr = ""
        temp = self.head
        while temp :
            LinkedlistStr += str(temp.data) + " "
            temp = temp.next
        return LinkedlistStr

if __name__ == "__main__":
    llist = Linkedlist()

    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print("Linkedlist: ")
    print(llist)

    print("after reverse: ")
    llist.head = llist.reverse(llist.head)
    print(llist)



# TC = O(n)
# SC = O(1)
