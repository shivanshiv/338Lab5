# 338 Lab 5 Exercise 3

import random
import timeit
import matplotlib.pyplot as plt

# 1) Stack using python lists
class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Empty stack - cannot pop")

    def is_empty(self):
        return len(self.items) == 0
        
# 2) Stack using singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty stack - cannot pop")
        value = self.head.value
        self.head = self.head.next
        return value

    def is_empty(self):
        return self.head is None

# 3) Generating random list of tasks
def generate_random_tasks(num_tasks=10000):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            tasks.append(('push', random.randint(1, 100)))
        else:
            tasks.append(('pop',))
    return tasks

# 4) Measuring performance
def measure_performance(stack_class, tasks):
    stack = stack_class()
    for task in tasks:
        if task[0] == 'push':
            stack.push(task[1])
        elif task[0] == 'pop':
            if not stack.is_empty():
                stack.pop()

def run_performance_tests(num_tests=100):
    array_times = []
    linked_list_times = []

    for _ in range(num_tests):
        tasks = generate_random_tasks()
        
        array_time = timeit.timeit(lambda: measure_performance(ArrayStack, tasks), number=1)
        array_times.append(array_time)

        linked_list_time = timeit.timeit(lambda: measure_performance(LinkedListStack, tasks), number=1)
        linked_list_times.append(linked_list_time)

    return array_times, linked_list_times

# 5) Plotting distribution
def plot_results(array_times, linked_list_times):
    plt.figure(figsize=(10, 6))
    plt.hist(array_times, bins=30, alpha=0.5, label='ArrayStack', color='blue', density=True)
    plt.hist(linked_list_times, bins=30, alpha=0.5, label='LinkedListStack', color='red', density=True)
    plt.title('Performance Comparison of Stack Implementations')
    plt.xlabel('Time (s)')
    plt.ylabel('Density (counts/s)')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    array_times, linked_list_times = run_performance_tests()
    plot_results(array_times, linked_list_times)
