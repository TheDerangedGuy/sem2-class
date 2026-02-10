#wap for queue underflow and overflow using class
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    
    def is_full(self):
        return len(self.queue) >= self.capacity
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue overflow! Cannot add item:", item)
        else:
            self.queue.append(item)
            print("Enqueued:", item)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow! Cannot remove item.")
        else:
            item = self.queue.pop(0)
            print("Dequeued:", item)
