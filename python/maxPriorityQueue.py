#Oliver Hamilton
#07/01/2020
#Priority queue

#Uses functionality defined in 'maxHeap.py'
from maxHeap import MaxHeap

#Priority queue implementation using max-heaps
class PriorityQueue:

    def __init__(self, arr, maxSize):
        #Call max heap constructor with parameters
        self.__maxHeap = MaxHeap(arr, maxSize)

    #Get the item with the highest priority in the queue
    def getHighestPriority(self):
        #If the heap is not empty
        if self.__maxHeap.heapSize > 0:
            #Return the root node of the max heap
            return self.__maxHeap.get(0)

        #Otherwise, output an error
        else:
            print("Priority queue is empty - item cannot be retrieved")

    #Return and delete the item with the highest priority in the queue
    def extractHighestPriority(self):
        n = self.__maxHeap.heapSize
        #If the heap is not empty
        if n > 0:
            #Get the root node of the max heap
            maxElement = self.__maxHeap.get(0)

            #Get the smallest element of the max heap
            smallestElement = self.__maxHeap.get(n - 1)

            #Replace the root node with the smallest element of the heap
            self.__maxHeap.set(0, smallestElement)

            #Reduce the size of the heap by one, so that the smallest element is removed
            self.__maxHeap.heapSize -= 1

            #Root node now violates max-heap property - call max heapify on root
            self.__maxHeap.maxHeapify(0)

            #Return the (deleted) maximum value
            return maxElement

        #Otherwise, output an error
        else:
            print("Priority queue is empty - item cannot be removed")

    #Insert a new item with its own priority
    def insertItem(self, newElement):
        #If the maximum heap size has been reached, the new item can't be inserted
        if self.__maxHeap.heapSize == self.__maxHeap.maxSize:
            print("Priority queue is full - item cannot be inserted")

        else:
            #Increment the heap size
            self.__maxHeap.heapSize += 1
            #Add the new item to the heap in the last array position
            self.__maxHeap.set(self.__maxHeap.heapSize - 1, newElement)

            #Call maxHeapify on parent nodes
            parentNode = self.__maxHeap.heapSize - 2 // 2

            while parentNode >= 0:
                print("Hello")
                self.__maxHeap.maxHeapify(parentNode)

                #Get next parent node to call maxHeapify on
                parentNode = (parentNode - 1) // 2

    #Output queue contents
    def output(self):
        #Call output method of max heap
        self.__maxHeap.output()

"""priorityQueue = PriorityQueue([1, 2, 3, 6], 30)
priorityQueue.output()
priorityQueue.insertItem(5)
priorityQueue.output()
print(priorityQueue.extractHighestPriority())
priorityQueue.output()
print(priorityQueue.extractHighestPriority())
priorityQueue.output()
print(priorityQueue.extractHighestPriority())
priorityQueue.output()
print(priorityQueue.extractHighestPriority())
priorityQueue.output()
print(priorityQueue.extractHighestPriority())
priorityQueue.output()
print(priorityQueue.extractHighestPriority())
priorityQueue.output()"""
