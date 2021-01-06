

# Link list node
class LNode :
	def __init__(self):
		self.data = None
		self.next = None

# A Binary Tree node
class TNode :
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None

head = None
def sortedListToBST():
	global head

	n = countLNodes(head)

	return sortedListToBSTRecur(n)

def sortedListToBSTRecur( n) :
	global head

	if (n <= 0) :
		return None

	left = sortedListToBSTRecur( int(n/2))
	root = newNode((head).data)
	root.left = left
	head = (head).next
	root.right = sortedListToBSTRecur( n - int(n/2) - 1)

	return root

def countLNodes(head) :

	count = 0
	temp = head
	while(temp != None):

		temp = temp.next
		count = count + 1

	return count

def push(head, new_data) :

	new_node = LNode()
	new_node.data = new_data
	new_node.next = (head)

	(head) = new_node
	return head

def printList(node):

	while(node != None):

		print( node.data ,end= " ")
		node = node.next

def newNode(data) :

	node = TNode()
	node.data = data
	node.left = None
	node.right = None

	return node

def preOrder( node) :

	if (node == None) :
		return
	print(node.data, end = " " )
	preOrder(node.left)
	preOrder(node.right)

# Driver code

head = None

head = push(head, 7)
head = push(head, 6)
head = push(head, 5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)
head = push(head, 1)

print("Given Linked List " )
printList(head)

root = sortedListToBST()
print("\nPreOrder Traversal of constructed BST ")
preOrder(root)

''' TC = O(n) '''
