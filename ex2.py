import random
import timeit
from bisect import insort

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
#1
class PriorityQueue1:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
        self.queue = mergesort(self.queue)
    
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
#2
class PriorityQueue2:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        insort(self.queue, value)  # Efficiently inserts while maintaining order
    
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
#3
def generate_task_list():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1, 10000)))
        else:
            tasks.append(("dequeue", None))
    return tasks
#4
def test_performance(queue_class):
    task_lists = [generate_task_list() for _ in range(100)]
    
    def run_test():
        queue = queue_class()
        for task, value in task_lists[0]:
            if task == "enqueue":
                queue.enqueue(value)
            else:
                queue.dequeue()
    
    return timeit.timeit(run_test, number=1)

pq1_time = test_performance(PriorityQueue1)
pq2_time = test_performance(PriorityQueue2)

print(f"PriorityQueue1 time: {pq1_time:.5f} seconds")
print(f"PriorityQueue2 time: {pq2_time:.5f} seconds")

# 5 - Discussion:
# PriorityQueue2 is expected to be faster because inserting elements in a sorted manner
# using insort() from the bisect module is more efficient (O(n) per insert) than appending
# and sorting the entire list using mergesort (O(n log n)).
# Thus, maintaining order at insertion is a better approach than sorting after each enqueue.
