class Stack:
  def __init__(self): # creates an empty stack
    self.items = []

  def push(self, item): # adds an item to the top of the stack
    self.items.append(item)

  def pop(self): # removes and returns the top item
    return self.items.pop()

  def peek(self): # returns the top item
    return self.items[-1]

  def is_empty(self): # returns True if the stack is empty
    return not self.items


  def __str__(self): # returns a string representation of the stack
        return str(self.items)


# Test the stack
stack = Stack() # creates an empty stack
# print(stack.is_empty())  # prints True (if the stack is empty)
stack.push(1) # adds 1 to the top of the stack
stack.push(2) # adds 2 to the top of the stack
stack.push(3) # adds 3 to the top of the stack
stack.push(5) # adds 5 to the top of the stack
print(stack)  # prints [1, 2, 3, 5]
print(stack.peek())    # prints 5
print(stack.pop())   # prints 5 and removes it from the stack
print(stack.is_empty()) # prints False (if the stack is not empty)