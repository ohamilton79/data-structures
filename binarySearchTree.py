#ohamilton79
#Binary tree implementation
#19/01/2020

#Node within the binary tree
class Node:
    def __init__(self, value, left=None, right=None):
        #Assign parameters to attributes
        self.value = value
        self.left = left
        self.right = right

    #Check if there is space for the new item to be inserted as a child of this node
    def spaceAvailable(self, newItem):
        #If there is space to the left of this node, and the item to be added is less than the value of this node
        if not self.left and newItem < self.value:
            return True

        #..or if there is space to the right of this node, and the item to be added is greater than the value of this node
        elif not self.right and newItem >= self.value:
            return True

        #Otherwise, there is no space for the item
        else:
            return False

#Class representing binary tree
class BinaryTree:

    #Define a new rootNode variable to store the root node
    def __init__(self):
        self.rootNode = None

    #Add a new item to the binary tree
    def addItem(self, newItem):
        #If the tree is empty, the item can be added as the root
        if self.rootNode == None:
            self.rootNode = Node(newItem)

        #If the tree isn't empty...
        else:
            #Start at the root node
            currentNode = self.rootNode

            #Keep traversing until the node has space for the item
            while not currentNode.spaceAvailable(newItem):
                #Traverse to the left if the new item is less than the value of the current node
                if newItem < currentNode.value:
                    currentNode = currentNode.left

                #Traverse to the right if the new item is more than the value of the current node
                else:
                    currentNode = currentNode.right

            #Insert the new item either to the left or right of this node, depending on its value
            if newItem < currentNode.value:
                currentNode.left = Node(newItem)

            else:
                currentNode.right = Node(newItem)

    #Remove an item from the binary tree
    def removeItem(self, itemToRemove):
        #Find the node being deleted
        currentNode = self.rootNode
        #While the current node exists, and isn't the one to delete
        while currentNode != None and currentNode.value != itemToRemove:
            #Set previous node to be current node
            previousNode = currentNode

            #If the item to be deleted is less than the current node's value, traverse the left branch
            if itemToRemove < currentNode.value:
                currentNode = currentNode.left

            #If the item to be deleted is greater than the current node's value, traverse the right branch
            else:
                currentNode = currentNode.right

        #If the node to be deleted has no children...
        if not currentNode.left and not currentNode.right:
            #If the current node is less than the previous node, set the previous node's left pointer to null
            if currentNode.value < previousNode.value:
                previousNode.left = None

            #If the current node is more than the previous node, set the previous node's right pointer to null
            else:
                previousNode.right = None

        #If the node to be deleted has one child...
        elif not currentNode.left or not currentNode.right:
            #Get the child of the node to be deleted
            childNode = None
            if currentNode.left:
                childNode = currentNode.left
            else:
                childNode = currentNode.right
                
            #If the current node is on the left of the previous node...
            if currentNode.value < previousNode.value:
                #Set the previous node's left pointer to point to the child of the deleted node
                previousNode.left = childNode

            #If the current node is on the right of the previous node...
            else:
                #Set the previous node's right pointer to point to the child of the deleted node
                previousNode.right = childNode

        #If the node to be deleted has two children, use Hibbard deletion method
        #(swap the node to be deleted with its successor)...
        else:
            rightNode = currentNode.right
            #Find the smallest node in the left subtree
            smallestNode = rightNode
            while smallestNode.left:
                smallestNode = smallestNode.left

            #Swap successor with node to be deleted, and recursively delete successor
            self.removeItem(smallestNode.value)
            currentNode.value = smallestNode.value
            
    #Perform a pre-order traversal of the binary tree
    def preOrderTraversal(self, node):
        #If the node has a value
        if node != None:
            #Output the value of the node
            print(node.value)

            #Traverse the left subtree
            self.preOrderTraversal(node.left)

            #Traverse the right subtree
            self.preOrderTraversal(node.right)

    #Perform an in-order traversal of the binary tree
    def inOrderTraversal(self, node):
        #If the node has a value
        if node != None:
            #Traverse the left subtree
            self.inOrderTraversal(node.left)
            
            #Output the value of the node
            print(node.value)

            #Traverse the right subtree
            self.inOrderTraversal(node.right)

    #Perform a post-order traversal of the binary tree
    def postOrderTraversal(self, node):
        #If the node has a value
        if node != None:
            #Traverse the left subtree
            self.postOrderTraversal(node.left)

            #Traverse the right subtree
            self.postOrderTraversal(node.right)

            #Output the value of the node
            print(node.value)

#Test data
binaryTree = BinaryTree()
binaryTree.addItem("F")
binaryTree.addItem("C")
binaryTree.addItem("P")
binaryTree.addItem("U")
binaryTree.addItem("V")
binaryTree.addItem("R")
binaryTree.addItem("S")
binaryTree.addItem("T")
binaryTree.addItem("G")
binaryTree.removeItem("P")
binaryTree.inOrderTraversal(binaryTree.rootNode)
