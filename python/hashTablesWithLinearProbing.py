#ohamilton79
#Hash tables with linear probing (closed hashing)
#24/01/2021

class HashTable:

    #Initialise an array of the maximum size with empty entries
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.tableArray = [None for i in range(maxSize)]

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

        #Apply linear probing to insert item
        currentIndex = hashValue
        count = 0
        while count != self.maxSize and self.tableArray[currentIndex] != None:
            currentIndex = (hashValue + 1) % self.maxSize
            count += 1

        #If the item can be added at this location
        if self.tableArray[currentIndex] == None:
            self.tableArray[hashValue] = newItem
            print("Item '{}' added successfully to the hash table".format(newItem))
            return True

        #If all indices have been checked, and the hash table is full
        else:
            print("Item '{}' could not be added to the hash table".format(newItem))
            return False

    #Traverse the hash table
    def traverse(self):
        #Iterate over each index in the table
        for i in range(self.maxSize):
            currentItem = self.tableArray[i]

            #Output this item if it isn't null
            if currentItem != None:
                print(currentItem)

    #Remove an item from the hash table
    def remove(self, itemToRemove):
        #Generate the hash value for this key to find the array index where it is stored
        hashValue = self.generateHash(itemToRemove)

        #Apply linear probing to delete item
        currentIndex = hashValue
        count = 0
        while currentIndex != hashValue and self.tableArray[currentIndex] != itemToRemove:
            currentIndex = (hashValue + 1) % self.maxSize
            count += 1

        #If the item can be removed at this location
        if self.tableArray[currentIndex] == itemToRemove:
            self.tableArray[hashValue] = None
            print("Item '{}' removed successfully from the hash table".format(itemToRemove))
            return True

        #If all indices have been checked, and the item can't be found
        else:
            print("Item '{}' could not be removed from the hash table".format(itemToRemove))
            return False

    #Search for an item in the hash table
    def search(self, searchItem):
        #Calculate its hash value, to get the table index
        hashValue = self.generateHash(searchItem)

        #Apply linear probing to search for item
        currentIndex = hashValue
        count = 0
        while currentIndex != hashValue and self.tableArray[currentIndex] != searchItem:
            currentIndex = (hashValue + 1) % self.maxSize
            count += 1

        #If the item being searched for is at this location
        if self.tableArray[currentIndex] == searchItem:
            print("Item '{}' found in the hash table at index {}".format(searchItem, currentIndex))
            return True

        #If all indices have been checked, and the item can't be found
        else:
            print("Item '{}' could not be found in the hash table".format(searchItem))
            return False


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
