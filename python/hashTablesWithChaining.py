#ohamilton79
#Hash tables with chaining (open hashing)
#20/01/2021

#Implement a linked list for chaining
class Node:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

class LinkedList:

    def __init__(self):
        self.head = None

    #Add a new item to the beginning of the list
    def addItem(self, newItem):
        #Check memory overflow
        try:
            #If the list is empty, make the head pointer point to this new item
            if self.head == None:
                self.head = Node(newItem)

            else:
                #Make this new node be at the front of the list, and point to the item that was previously at the front
                temp = self.head
                self.head = Node(newItem, temp)

            return True
        #Return false if the item couldn't be added (memory overflow)
        except:
            return False

    #Traverse the linked list
    def traverse(self):
        #Start at the head pointer (start of list)
        currentNode = self.head

        #Continue until node is null
        while currentNode != None:
            #Output current node's value
            print(currentNode.value)
            #Get next node
            currentNode = currentNode.pointer

    #Remove an item from the linked list
    def removeItem(self, itemToRemove):
        #Check list isn't empty
        if self.head != None:
            #If the item is at the start of the list, the value of the head pointer can simply be changed
            if self.head.value == itemToRemove:
                self.head = self.head.pointer
                return True

            else:
                #Search for the item in the linked list by traversing nodes sequentially
                currentNode == self.head
                #While the end of the list hasn't been reached and the item hasn't been found
                while currentNode != None and currentNode.value != itemToRemove:
                    previousNode = currentNode
                    currentNode = currentNode.pointer

                #If the current node is null, the item doesn't exist in the list
                if currentNode == None:
                    return False

                #Otherwise, set the previous node to point to the node after the current node, bypassing it
                else:
                    previousNode.pointer = currentNode.pointer
                    return True

        #Return false if the list is empty
        else:
            return False

    #Search for an item in the linked list
    def search(self, searchItem):
        #Start at the head pointer (start of list)
        currentNode = self.head

        #By default, the index of the item is -1 if not found
        index = -1

        found = False

        #Counter to identify list index
        counter = 0

        #Continue until node is null or item found
        while currentNode != None and not found:
            #If the value of this node is the search item, the item has been found
            if currentNode.value == searchItem:
                #Set index where item is in list
                index = counter
                #Set flag to exit while loop
                found = True

            #Get next node to check
            currentNode = currentNode.pointer
            #Increment counter so that next list index can be checked
            counter += 1

        #Return the item's index
        return index
                

class HashTable:

    #Initialise an array of the maximum size of empty linked lists
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.tableArray = [LinkedList() for i in range(maxSize)]

    #Generate the hash value for a given item (key)
    def generateHash(self, key):
        #Get the sum of the ASCII character codes of the key
        sumOfChars = sum([ord(char) for char in key])

        #Get the remainder when divided by the size of the hash table
        hashValue = sumOfChars % self.maxSize

        return hashValue

    #Add an item to the hash table
    def addItem(self, newItem):
        #Generate the hash value (table index) from the item to be added
        hashValue = self.generateHash(newItem)

        #Add the item to the linked list at this location
        if self.tableArray[hashValue].addItem(newItem):
            print("Item '{}' added successfully to the hash table".format(newItem))
            return True

        else:
            print("Item '{}' could not be added to the hash table".format(newItem))
            return False

    #Traverse the hash table
    def traverse(self):
        #Iterate over each index in the table
        for i in range(self.maxSize):
            currentList = self.tableArray[i]

            #Traverse the linked list at this location
            currentList.traverse()

    #Remove an item from the hash table
    def remove(self, itemToRemove):
        #Generate the hash value for this key to find the array index where it is stored
        hashValue = self.generateHash(itemToRemove)
        #Get the linked list at this location
        linkedList = self.tableArray[hashValue]
        #Delete the item from this linked list
        if linkedList.removeItem(itemToRemove):
            print("Item '{}' successfully deleted from the hash table".format(itemToRemove))
            return True
        else:
            print("Item '{}' could not be deleted from the hash table".format(itemToRemove))
            return False

    #Search for an item in the hash table
    def search(self, searchItem):
        #Calculate its hash value, to get the table index
        hashValue = self.generateHash(searchItem)

        #Get the linked list at this location
        linkedList = self.tableArray[hashValue]

        #Get index of item in linked list
        linkedListIndex = linkedList.search(searchItem)

        if linkedListIndex != -1:
            print("Item '{}' found at index {} of the linked list at the hash table index {}".format(searchItem, linkedListIndex, hashValue))
            return True

        else:
            print("Item '{}' not found in hash table".format(searchItem))

#Test data
hashTable = HashTable(31)
hashTable.traverse()
hashTable.addItem("John")
hashTable.search("John")
hashTable.search("Jack")
hashTable.traverse()
hashTable.addItem("Maria")
hashTable.traverse()
hashTable.remove("John")
hashTable.traverse()
hashTable.remove("Jack")
hashTable.traverse()




