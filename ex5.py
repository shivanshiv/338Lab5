class CircularQueueArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("enqueue None")  # Queue is full
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"enqueue {value}")
    
    def dequeue(self):
        if self.front == -1:
            print("dequeue None")
            return None
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"dequeue {value}")
        return value
    
    def peek(self):
        if self.front == -1:
            print("peek None")
            return None
        print(f"peek {self.queue[self.front]}")
        return self.queue[self.front]

class CircularQueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueueLinkedList:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.front = self.rear = None
    
    def enqueue(self, value):
        if self.count == self.size:
            print("enqueue None")
            return
        new_node = CircularQueueNode(value)
        if not self.front:
            self.front = self.rear = new_node
            self.rear.next = self.front  # Circular link
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        self.count += 1
        print(f"enqueue {value}")
    
    def dequeue(self):
        if self.count == 0:
            print("dequeue None")
            return None
        value = self.front.value
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.count -= 1
        print(f"dequeue {value}")
        return value
    
    def peek(self):
        if self.count == 0:
            print("peek None")
            return None
        print(f"peek {self.front.value}")
        return self.front.value

def test_circular_queues():
    cq = CircularQueueArray(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)  # Full queue
    cq.peek()
    cq.dequeue()
    cq.dequeue()
    cq.enqueue(6)
    cq.enqueue(7)  # Wraps around
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()  # Empty queue

test_circular_queues()
