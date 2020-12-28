from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack")

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)  # return minus infinity
    return stack.pop()

def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)

    return stack[len(stack) - 1]

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))

print(pop(stack) + " popped from stack")
print("top element is: ",peek(stack))

# Pros: Easy to implement. Memory is saved as pointers are not involved.

# Cons: It is not dynamic. It doesn’t grow and shrink depending
# on needs at runtime.
