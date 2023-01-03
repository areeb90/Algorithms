class Node:                     #Create a Node class
    def __init__(self, data):   #Initialize the Node class
        self.data = data        #Set the data attribute
        self.next = None        #Set the next attribute
        self.prev = None        #Set the prev attribute
    
    def __str__(self):              #Create a __str__ method
        return str(self.data)       #Return the data attribute


class doublyLinkedList:     #Create a doublyLinkedList class
    def __init__(self):     #Initialize the doublyLinkedList class
        self.head = None    #Set the head attribute
        self.tail = None    #Set the tail attribute



    def insertionAtHead(self, data):    #Insertion at the head of the list  

        newNode = Node(data)            #Create a new node
        if self.head is None:           #If the head is None
            self.head = newNode         #Set the head to the new node
            self.tail = newNode         #Set the tail to the new node
        else:                       #If the head is not None
            newNode.next = self.head    #Set the new node's next to the head
            self.head.prev = newNode    #Set the head's prev to the new node
            self.head = newNode         #Set the head to the new node
        


    def insertionAtTail(self, data):    #Insertion at the tail of the list

        newNode = Node(data)            #Create a new node
        if self.tail is None:           #If the tail is None
            self.head = newNode         #Set the head to the new node
            self.tail = newNode         #Set the tail to the new node
        else:                           #If the tail is not None
            newNode.prev = self.tail    #Set the new node's prev to the tail
            self.tail.next = newNode    #Set the tail's next to the new node
            self.tail = newNode         #Set the tail to the new node





    def traversal(self):    #Traversal of the list
        
        if self.head is None:   #If the head is None
            return "The list is empty"  #Return the list is empty
        else:                   #If the head is not None
            currentNode = self.head     #Set the currentNode to the head
            while currentNode is not None:  #While the currentNode is not None
                print(currentNode.data)     #Print the currentNode's data
                currentNode = currentNode.next  #Set the currentNode to the currentNode's next
            return "Traversal is complete"

            



DLL = doublyLinkedList()
DLL.insertionAtHead(1)
DLL.insertionAtHead(2)
DLL.insertionAtHead(3)
DLL.insertionAtTail(4)
print(DLL.traversal())