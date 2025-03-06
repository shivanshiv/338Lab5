import random
import timeit
import matplotlib.pyplot as plt

class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.insert(0, value)  # Insert at head (O(n))
    
    def dequeue(self):
        return self.queue.pop() if self.queue else None  # Remove from tail (O(1))

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        
        if prev:
            prev.next = None
            self.tail = prev
        else:
            self.head = self.tail = None
        
        return current.value

def generate_task_list():
    tasks = []
    for _ in range(10000):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1, 10000)))
        else:
            tasks.append(("dequeue", None))
    return tasks

def test_performance(queue_class):
    task_lists = [generate_task_list() for _ in range(100)]
    
    times = []
    for task_list in task_lists:
        queue = queue_class()
        start = timeit.default_timer()
        for task, value in task_list:
            if task == "enqueue":
                queue.enqueue(value)
            else:
                queue.dequeue()
        end = timeit.default_timer()
        times.append(end - start)
    
    return times

array_queue_times = test_performance(ArrayQueue)
linked_list_queue_times = test_performance(LinkedListQueue)

plt.hist(array_queue_times, bins=30, alpha=0.5, label='ArrayQueue')
plt.hist(linked_list_queue_times, bins=30, alpha=0.5, label='LinkedListQueue')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.title('Queue Performance Comparison')
plt.show()

# Discussion:
# The ArrayQueue implementation suffers from O(n) complexity when inserting at the head,
# making it inefficient for large operations. However, dequeuing is O(1).
# The LinkedListQueue is more balanced, as inserting at the head is O(1), but removing from the tail
# requires traversing the list (O(n)).
# Based on the histogram, we expect the LinkedListQueue to have a more stable distribution,
# whereas the ArrayQueue might show higher variance and longer runtimes.
