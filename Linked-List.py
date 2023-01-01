class Node:                     # Node class
  def __init__(self, value):    # creates a node
    self.value = value          # stores the value
    self.next = None            # stores the reference to the next node

class LinkedList:       # LinkedList class
  def __init__(self):   # creates an empty linked list
    self.head = None    # stores the reference to the first node

  def append(self, value):  # adds a new node containing value at the end
    new_node = Node(value)  # creates a new node
    if self.head is None:   # if the linked list is empty
      self.head = new_node  # make the new node the head
      return                # and exit the function

    current_node = self.head                # start from the head node
    while current_node.next is not None:    # iterate to the end of the list 
      current_node = current_node.next      # update the reference to the current node
    current_node.next = new_node            # set the new node as the next node of the last node


  def prepend(self, value):     # adds a new node containing value at the beginning
    new_node = Node(value)      # creates a new node
    new_node.next = self.head   # set the new node's next reference to the current head
    self.head = new_node        # set the head reference to the new node


  def delete_with_value(self, value):   # deletes the first node with the given value
    if self.head is None:               # if the linked list is empty
      return                            # exit the function
    if self.head.value == value:        # if the head node contains the value
      self.head = self.head.next        # set the head reference to the next node
      return                            # and exit the function
    current_node = self.head            # start from the head node
    while current_node.next is not None:    # iterate to the end of the list
      if current_node.next.value == value:  # if the next node contains the value
        current_node.next = current_node.next.next  # set the next reference to the next node's next node
        return                                      # and exit the function
      current_node = current_node.next              # update the reference to the current node



  def to_list(self):                    # converts the linked list to a Python list
    current_node = self.head            # start from the head node
    result = []                         # create an empty list
    while current_node is not None:     # iterate to the end of the list
      result.append(current_node.value) # append the current node's value to the result list
      current_node = current_node.next  # update the reference to the current node
    return result                       # return the result list


    
  def traversal(self):                  # converts the linked list to a Python list
        current_node = self.head            # start from the head node
        while current_node is not None:     # iterate to the end of the list
            print(current_node.value) # append the current node's value to the result list
            current_node = current_node.next  # update the reference to the current node
        return current_node                       # return the result list



  def insert_at_the_begining(self, value):
    new_node = Node(value)      # creates a new node
    new_node.next = self.head   # set the new node's next reference to the current head
    self.head = new_node        # set the head reference to the new node



  def insert_at_the_middle(self, value):    # adds a new node containing value at the beginning
    tortoise = self.head                    # set the new node's next reference to the current head
    hare = self.head                        # set the head reference to the new node
    while hare is not None and hare.next is not None:   # iterate to the end of the list
        tortoise = tortoise.next                        # update the reference to the current node
        hare = hare.next.next                           # update the reference to the current node                                  

    new_node = Node(value)                  # creates a new node
    new_node.next = tortoise.next           # set the new node's next reference to the current head
    tortoise.next = new_node                # set the head reference to the new node



  def insert_at_the_end(self, value):
    new_node = Node(value)  # creates a new node
    if self.head is None:   # if the linked list is empty
      self.head = new_node  # make the new node the head
      return                # and exit the function

    current_node = self.head                # start from the head node
    while current_node.next is not None:    # iterate to the end of the list 
      current_node = current_node.next      # update the reference to the current node
    current_node.next = new_node            # set the new node as the next node of the last node



  def search(self, key):            # converts the linked list to a Python list
    current = self.head             # start from the head node

    while current is not None:      # iterate to the end of the list
        if current.value == key:    # if the next node contains the value
            return True             # return True
        current = current.next      # update the reference to the current node

    return False                    # return False



  def sort(self):           # converts the linked list to a Python list
    current = self.head     # start from the head node
    index = None            # start from the head node

    if self.head is None:   # if the linked list is empty
        return              # exit the function
    else:                   # if the linked list is not empty
        while current is not None:  # iterate to the end of the list
            index = current.next    # update the reference to the current node

            while index is not None:    # iterate to the end of the list
                if current.value > index.value: # if the next node contains the value
                    temp = current.value        # update the reference to the current node
                    current.value = index.value # update the reference to the current node
                    index.value = temp          # update the reference to the current node
                index = index.next              # update the reference to the current node

            current = current.next              # update the reference to the current node





  def delete_at_the_begining(self):
    if self.head is None:               # if the linked list is empty
      return                            # exit the function
    else:
        self.head = self.head.next      # set the head reference to the next node
        return                          # and exit the function



  def delete_at_the_middle(self):
    tortoise = self.head                    # set the new node's next reference to the current head
    hare = self.head                        # set the head reference to the new node
    while hare is not None and hare.next is not None:   # iterate to the end of the list
        tortoise = tortoise.next                        # update the reference to the current node
        hare = hare.next.next                           # update the reference to the current node                                  

    tortoise.next = tortoise.next.next           # set the new node's next reference to the current head



  def delete_at_the_end(self):
    if self.head is None:               # if the linked list is empty
      return                            # exit the function
    else:
        current_node = self.head                # start from the head node
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None                # set the new node as the next node of the last node





# Test the linked list

linked_list = LinkedList() # creates an empty linked list

linked_list.append(1)       # adds 1 to the end of the list
linked_list.append(2)       # adds 2 to the end of the list
# linked_list.prepend(0)      # adds 0 to the beginning of the list
linked_list.append(7)       # adds 7 to the end of the list
linked_list.append(4)        
linked_list.append(6)       
linked_list.append(3)        
linked_list.append(8)
linked_list.append(5)         


linked_list.sort()


print(linked_list.to_list())
print(linked_list.delete_at_the_begining())
print(linked_list.to_list())

print(linked_list.to_list())
print(linked_list.delete_at_the_middle())
print(linked_list.to_list())

print(linked_list.to_list())
print(linked_list.delete_at_the_end())
print(linked_list.to_list())

print (linked_list.traversal())
print(linked_list.to_list())    # prints [0, 1, 2, 7]

linked_list.insert_at_the_middle(4)
print(linked_list.to_list())   #print [0, 1, 2, 4, 5, 7]

linked_list.insert_at_the_end(6)
print(linked_list.to_list())

print(linked_list.search(8))
linked_list.delete_with_value(1)        # deletes the first node with the value 1
print(linked_list.to_list())     
