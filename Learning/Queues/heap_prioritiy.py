import heapq

# Basic heap test using a list

basic_heap = [5,1,6,7,3,10]

heapq.heapify(basic_heap)

print(basic_heap)

# Pushing elements to a heap, leads to an unordered list somehow

heapq.heappush(basic_heap, 2)

print(basic_heap)

# Building a simple priority queue class with push and pop methods

class PriorityQueue:
    def __init__(self):
        # Again using a list to store heap elements
        self.heap = []
        
        # Defining a push method
    def push(self, priority):
        heapq.heappush(self.heap, (priority))

    def pop(self):
        return heapq.heappop(self.heap)

# Push three tasks with different priorities
pq = PriorityQueue()
pq.push(10)
pq.push(2)
pq.push(1)
pq.push(1.5)


print(pq.pop())  
print(pq.pop()) 
print(pq.pop())  
print(pq.pop())
