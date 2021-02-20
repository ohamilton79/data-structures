#ohamilton79
#Min heap
#20/01/2021

#Define a class representing a min-heap, so that a priority queue can be implemented
class MinHeap:

    def __init__(self, arr, maxSize):
        #Define the size of the heap
        self.maxSize = maxSize
        self.heapSize = len(arr)

        #Define a dictionary mapping from heap elements to array indices
        self.elementMapping = {}
        
        #Initialise array with defined size and empty entries
        self.__heapArray = [None]*self.maxSize

        #Add elements passed to heap array
        for index, element in enumerate(arr):
            self.__heapArray[index] = element
            self.elementMapping[element[1]] = index

        #Create the min heap
        self.buildMinHeap()

    #Get a value at a given index in the heap
    def getValue(self, index):
        return self.__heapArray[index][1]

    #Set a value at a given index in the heap
    def setValue(self, index, val):
        self.__heapArray[index][1] = val

    #Get the key at a given index in the heap
    def getKey(self, index):
        return self.__heapArray[index][0]

    #Set the key at a given index in the heap
    def setKey(self, index, val):
        self.__heapArray[index][0] = val
        
    def buildMinHeap(self):
        #Min-heapify the array
        n = self.heapSize

        #If the heap isn't empty
        if not n == 0:
            #Iterate over elements that aren't leaves
            for i in range(n // 2, -1, -1):
                self.minHeapify(i)

    #Fix a single violation of the min-heap property for subtree with a root at A[i]
    def minHeapify(self, i):
        leftNode = 2*i + 1
        rightNode = 2*i + 2
        #By default, the min node is the root node of this subtree
        minNode = i

        #If the left child's priority is less than the root of the subtree
        if leftNode < self.heapSize and self.getKey(leftNode) < self.getKey(minNode):
            minNode = leftNode

        #If the right child is less than the root of the subtree
        if rightNode < self.heapSize and self.getKey(rightNode) < self.getKey(minNode):
            minNode = rightNode

        #If one of the children is the minimum node
        if minNode != i:
            #Update elements mapping and swap the values and keys at the root node and minimum node
            self.elementMapping[self.__heapArray[minNode][1]] = i
            self.elementMapping[self.__heapArray[i][1]] = minNode
            
            temp = self.__heapArray[minNode]
            self.__heapArray[minNode] = self.__heapArray[i]
            self.__heapArray[i] = temp

            #Call minHeapify on the subtree where the minimum child node is the root node
            self.minHeapify(minNode)

    #Insert an item into the min-heap
    def insertItem(self, newItem):
        #Check for overflow
        if self.maxSize == self.heapSize:
            print("Item cannot be inserted - heap is full")
        else:
            #Add the new item to the end of the heap array
            self.heapSize += 1
            self.__heapArray[self.heapSize - 1] = newItem

            #Update mapping from elements to array indices
            self.elementMapping[newItem[1]] = self.heapSize - 1

            #Keep swapping the item with its parent if its key is smaller
            currentNode = self.heapSize - 1
            parentNode = (currentNode - 1) // 2

            #Whilst the top of the heap hasn't been reached
            while parentNode >=0:
                #Min-heap property now satisfied
                if self.getKey(currentNode) > self.getKey(parentNode):
                    break
                else:
                    #Otherwise, update elements mapping and swap current node and parent node
                    self.elementMapping[self.getValue(currentNode)] = parentNode
                    self.elementMapping[self.getValue(parentNode)] = currentNode
                    
                    temp = self.__heapArray[currentNode]
                    self.__heapArray[currentNode] = self.__heapArray[parentNode]
                    self.__heapArray[parentNode] = temp

                    #Prepare for next iteration
                    currentNode = parentNode
                    parentNode = (currentNode - 1) // 2

    #Extract and return the minimum element from the min-heap
    def extractMin(self):
        #Check if the heap is empty
        if self.heapSize <= 0:
            print("Heap is empty - minimum element cannot be extracted")

        else:
            #Swap the minimum element with the last element
            minElement = self.__heapArray[0]
            self.__heapArray[0] = self.__heapArray[self.heapSize - 1]
            self.__heapArray[self.heapSize - 1] = minElement
            #Update the mapping from elements to array indices by removing the deleted element's key and swapping the first and last element's indices
            self.elementMapping[self.__heapArray[self.heapSize - 1][1]] = 0
            self.elementMapping.pop(minElement[1])

            #Decrement the size of the heap, removing the last element
            self.heapSize -= 1

            #Run min-heapify on the new root, as its children are min-heaps
            self.minHeapify(0)

            #Return the minimum element
            return minElement

    #Decrease the key of an element in the min-heap
    def decreaseKey(self, element, key):
        #Map the element to an index in the array
        currentNode = self.elementMapping[element]

        #Get the previous key stored for this element
        previousKey = self.getKey(currentNode)
        
        #The new key cannot be more than the previous key
        if key > previousKey:
            print("The new key cannot be more than the current key")

        else:
            #Update the element's key
            self.setKey(currentNode, key)
            
            parentNode = (currentNode - 1) // 2
            #While the parent node's key is greater than the child node's...
            while currentNode > 0 and self.getKey(parentNode) > self.getKey(currentNode):
                #Swap elements and update elements mapping
                self.elementMapping[self.getValue(currentNode)] = parentNode
                self.elementMapping[self.getValue(parentNode)] = currentNode

                temp = self.__heapArray[currentNode]
                self.__heapArray[currentNode] = self.__heapArray[parentNode]
                self.__heapArray[parentNode] = temp
                
                #Compare further up the tree
                currentNode = parentNode
                parentNode = (currentNode - 1) // 2
