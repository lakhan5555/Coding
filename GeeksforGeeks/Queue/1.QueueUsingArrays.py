class Queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.capacity = capacity
        self.Q = [None]*capacity
        self.rear = capacity - 1

    def isFull(self):
        return self.capacity == self.size

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self,item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1)%self.capacity
        self.Q[self.rear] = item
        self.size += 1
        print("%d enqueued to queue"%(item))

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return
        print("%d dequeued from queue"%(self.Q[self.front]))
        self.front = (self.front + 1)%self.capacity
        self.size -= 1

    def que_front(self):
        if self.isEmpty():
            print("Empty")
            return
        print("front item is: ",self.Q[self.front])

    def que_rear(self):
        if self.isEmpty():
            print("Empty")
            return
        print("rear item is: ",self.Q[self.rear])

if __name__ == "__main__":
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
