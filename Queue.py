class Queue:                    # Queue class
    def __init__(self):         # Constructor
        self.items = []         # Create an empty list

    def isEmpty(self):          # Check if the queue is empty
        return self.items == [] # Return True if empty

    def enqueue(self, item):    # Add an item to the queue
        self.items.insert(0,item)   # Insert the item at the front of the list

    def dequeue(self):           # Remove an item from the queue
        return self.items.pop()  # Remove the last item from the list

    def size(self):             # Return the size of the queue
        return len(self.items)  # Return the length of the list

    def __str__(self):          # Return the string representation of the queue
        return str(self.items)  # Return the string representation of the list

    def __repr__(self):         # Return the string representation of the queue
        return str(self.items)  # Return the string representation of the list

    def peek(self):             # Return the first item in the queue
        return self.items[-1]   # Return the last item in the list




#TEST CODE

queue = Queue()            # Create a queue
queue.enqueue(1)            # Add items to the queue      
queue.enqueue(2)            # Add items to the queue
queue.enqueue(5)            
queue.enqueue(7)
queue.enqueue(3)


print(queue)
print(queue.dequeue())     # Remove an item from the queue
print(queue)                # Print the queue

print(queue)
print(queue.peek())     # Print the first item in the queue
print(queue)

print(queue)
print(queue.size())     # Print the size of the queue
print(queue)

