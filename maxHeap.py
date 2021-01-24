class MaxHeap:

    def __init__(self, arr, maxSize):
        #Define the size of the heap
        self.heapSize = len(arr)
        self.maxSize = maxSize
        #Initialise array with defined size and empty entries
        self.__heapArray = [None]*maxSize
        
        #Add elements passed to heap array
        for index, element in enumerate(arr):
            self.__heapArray[index] = element
            
        #Create the max heap
        self.buildMaxHeap()

    #Get a value at a given index in the heap
    def get(self, index):
        return self.__heapArray[index]

    #Set a value at a given index in the heap
    def set(self, index, val):
        self.__heapArray[index] = val

    def buildMaxHeap(self):
        #Max heapify the array
        n = self.heapSize
        for i in range(n // 2, -1, -1):
            self.maxHeapify(i)

    #Fix a single violation of the max-heap property for subtree with a root at A[i]
    def maxHeapify(self, i):
        leftNode = 2*i + 1
        rightNode = 2*i + 2
        #By default, the maximum node is the root node of this subtree
        maxNode = i

        #If the left child is greater than the root of the subtree
        if leftNode < self.heapSize and self.get(leftNode) > self.get(maxNode):
            maxNode = leftNode

        #If the right child is greater than the root node of the subtree
        if rightNode < self.heapSize and self.get(rightNode) > self.get(maxNode):
            maxNode = rightNode

        #If one of the children is the maximum node
        if maxNode != i:
            #Swap the values at the root node and maximum child node
            temp = self.get(maxNode)
            self.set(maxNode, self.get(i))
            self.set(i, temp)

            #Call maxHeapify on the subtree where the maximum child node is the root node
            self.maxHeapify(maxNode)

    #Output the array representation of the heap
    def output(self):
        print([self.__heapArray[i] for i in range(self.heapSize)])


#Create a new max heap
#testArr = [1, 2, 5, 8, 10, 12, 15]
#maxHeap = MaxHeap(testArr)
#maxHeap.output()

        
