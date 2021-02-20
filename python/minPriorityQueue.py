#ohamilton79
#Min priority queue
#20/01/2021

#Uses functionality defined in 'minHeap.py' file
from minHeap import MinHeap

class MinPriorityQueue:

    def __init__(self, arr, maxSize):
        #Call min heap constructor using parameters
        self.__minHeap = MinHeap(arr, maxSize)

    #Get the priority associated with a given element
    def getPriority(self, element):
        #Map the element to its array index
        index = self.__minHeap.elementMapping[element]

        #Return the priority
        return self.__minHeap.getKey(index)

    #Get the item with the lowest priority in the queue
    def getLowestPriority(self):
        #If the heap is not empty
        if self.__minHeap.heapSize > 0:
            #Return the root node of the min heap
            return self.__minHeap.__heapArray[0]

        #Otherwise, output an error
        else:
            print("Priority queue is empty - item cannot be retrieved")

    #Return and delete the item with the lowest priority in the queue
    def extractMinPriority(self):
        #Extract the item with the minimum key in the heap
        item = self.__minHeap.extractMin()

        return item

    #Insert a new item with its own priority
    def insertItem(self, priority, value):
        #Compile the value and priority into a single array
        item = [priority, value]

        #Insert the item into the min heap
        self.__minHeap.insertItem(item)

    #Decrease the priority to a new value for an element in the min-heap
    def decreaseKey(self, element, priority):
        self.__minHeap.decreaseKey(element, priority)

    #Check if the priority queue is empty
    def isEmpty(self):
        if self.__minHeap.heapSize > 0:
            return False

        else:
            return True

    #Check if an element is in the queue
    def contains(self, element):
        if element in self.__minHeap.elementMapping:
            return True

        else:
            return False
