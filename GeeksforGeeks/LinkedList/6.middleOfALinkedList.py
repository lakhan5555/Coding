# Given a singly linked list, find the middle of the linked list

# If there are even nodes, then there would be two middle nodes,
# we need to print the second middle element

# method 1

# Traverse the whole linked list and count the no. of nodes.
# Now traverse the list again till count/2 and return the node at count/2.


# method 2

# Traverse linked list using two pointers
# Move one pointer by one and the other pointers by two
# When the fast pointer reaches the end
# slow pointer will reach the middle of the linked list.

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

    def middle(self):
        slow = self.head
        fast = self.head

        if(self.head is not None):
            while (fast != None and fast.next != None):
                slow = slow.next
                fast = fast.next.next

            print("middle element is: ", slow.data)

if __name__ == "__main__":

    llist = Linkedlist()

    for i in range(5,0,-1):
        llist.push(i)

    llist.middle()
