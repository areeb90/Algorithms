class Node:  # Create a Node class
    def __init__(self, data):  # Initialize the Node class
        self.data = data  # Set the data attribute
        self.next = None  # Set the next attribute
        self.prev = None  # Set the prev attribute

    def __str__(self):  # Create a __str__ method
        return str(self.data)  # Return the data attribute


class doublyLinkedList:  # Create a doublyLinkedList class
    def __init__(self):  # Initialize the doublyLinkedList class
        self.head = None  # Set the head attribute
        self.tail = None  # Set the tail attribute



    def insertionAtHead(self, data):    # Insertion at the head of the list

        newNode = Node(data)            # Create a new node
        if self.head is None:           # If the head is None
            self.head = newNode         # Set the head to the new node
            self.tail = newNode         # Set the tail to the new node
        else:                           # If the head is not None
            newNode.next = self.head    # Set the new node's next to the head
            self.head.prev = newNode    # Set the head's prev to the new node
            self.head = newNode         # Set the head to the new node



    def insertionAtTail(self, data):    # Insertion at the tail of the list

        newNode = Node(data)            # Create a new node
        if self.tail is None:           # If the tail is None
            self.head = newNode         # Set the head to the new node
            self.tail = newNode         # Set the tail to the new node
        else:                           # If the tail is not None
            newNode.prev = self.tail    # Set the new node's prev to the tail
            self.tail.next = newNode    # Set the tail's next to the new node
            self.tail = newNode         # Set the tail to the new node



    def insert_at_specific_position(self, data, position):

        newNode = Node(data)                # Create a new node
        if self.head is None:               # If the head is None
            self.head = newNode             # Set the head to the new node
            self.tail = newNode             # Set the tail to the new node
        else:                               # If the head is not None
            currentNode = self.head         # Set the currentNode to the head
            currentPosition = 0             # Set the currentPosition to 0
            while currentNode is not None:  # While the currentNode is not None
                if currentPosition == position:     # If the currentPosition is equal to the position
                    newNode.next = currentNode      # Set the new node's next to the currentNode
                    newNode.prev = currentNode.prev # Set the new node's prev to the currentNode's prev
                    currentNode.prev.next = newNode # Set the currentNode's prev's next to the new node
                    currentNode.prev = newNode      # Set the currentNode's prev to the new node
                currentNode = currentNode.next      # Set the currentNode to the currentNode's next
                currentPosition += 1                # Increment the currentPosition by 1



    def traversal(self):                        # Traversal of the list

        if self.head is None:                   # If the head is None
            return "The list is empty"          # Return the list is empty
        else:                                   # If the head is not None
            currentNode = self.head             # Set the currentNode to the head
            while currentNode is not None:      # While the currentNode is not None
                print(currentNode.data)         # Print the currentNode's data
                currentNode = currentNode.next  # Set the currentNode to the currentNode's next
            return "Traversal is complete"



    def reverseTraversal(self):                 # Reverse traversal of the list

        if self.tail is None:                   # If the tail is None
            return "The list is empty"          # Return the list is empty
        else:                                   # If the tail is not None
            currentNode = self.tail             # Set the currentNode to the tail
            while currentNode is not None:      # While the currentNode is not None
                print(currentNode.data)         # Print the currentNode's data
                currentNode = currentNode.prev  # Set the currentNode to the currentNode's prev
            return "Reverse traversal is complete"



    def deletionAtHead(self):               # Deletion at the head of the list

        if self.head is None:               # If the head is None
            return "The list is empty"
        else:                               # If the head is not None
            self.head = self.head.next      # Set the head to the head's next
            self.head.prev = None           # Set the head's prev to None
        return "Deletion at Head is complete"



    def deletionAtTail(self):               # Deletion at the tail of the list

        if self.tail is None:               # If the tail is None
            return "The list is empty"
        else:                               # If the tail is not None
            self.tail = self.tail.prev      # Set the tail to the tail's prev
            self.tail.next = None           # Set the tail's next to None
        return "Deletion at Tail is complete"



    def delete_specific_node(self, data):
        if self.head is None:                       # If the head is None
            return "The list is empty"

        else:                                       # If the head is not None
            currentNode = self.head                 # Set the currentNode to the head
            while currentNode is not None:          # While the currentNode is not None
                if currentNode.data == data:        # If the currentNode's data is equal to the data
                    # Set the currentNode's prev's next to the currentNode's next
                    currentNode.prev.next = currentNode.next
                    # Set the currentNode's next's prev to the currentNode's prev
                    currentNode.next.prev = currentNode.prev

                # Set the currentNode to the currentNode's next
                currentNode = currentNode.next
            # Return the deletion is complete
            return "Deletion is complete"



    def search(self, data):                     # Search for a node in the list

        if self.head is None:                   # If the head is None
            return "The list is empty"
        else:                                   # If the head is not None
            currentNode = self.head             # Set the currentNode to the head
            while currentNode is not None:      # While the currentNode is not None
                if currentNode.data == data:    # If the currentNode's data is equal to the data
                    return "Key Exist"          # Return the key exist
                currentNode = currentNode.next  # Set the currentNode to the currentNode's next

            return "Key does not exist"         # Return the key does not exist






# TEST CASES
DLL = doublyLinkedList()
DLL.insertionAtHead(1)
DLL.insertionAtHead(2)
DLL.insertionAtHead(3)
DLL.insertionAtHead(4)
DLL.insertionAtHead(5)
DLL.insertionAtHead(6)
# DLL.insertionAtTail(4)

print(DLL.traversal())
print(DLL.reverseTraversal())

print(DLL.traversal())
print(DLL.deletionAtHead())
print(DLL.traversal())


print(DLL.traversal())
print(DLL.deletionAtTail())
print(DLL.traversal())

print(DLL.traversal())
print(DLL.search(3))


print(DLL.traversal())
print(DLL.delete_specific_node(2))        # Delete node with data 2
print(DLL.traversal())                    # Print the list after deletion is complete 


print(DLL.traversal())
print(DLL.insert_at_specific_position(2, 1))    # Insert 2 at position 1
print(DLL.traversal())                          # Print the list after insertion at position 1 is complete 