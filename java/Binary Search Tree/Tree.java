public class Tree {

    //Points to the root node of the tree
    Node rootNode = null;

    //Empty constructor
    public Tree() {
    }

    public void addItem(String newItem) {
        Node newNode = new Node(newItem);
        //1. Check if the root node is null, and if so add this new node as the root node
        if (rootNode == null) {
            this.rootNode = newNode;
            return;
        }

        //2. Set the root node as the current node
        Node currentNode = rootNode;

        //Keep traversing until the item can be inserted
        while (!currentNode.spaceAvailable(newItem)) {

            //3. Traverse to left if new item is less than the value of the current node
            if (newItem.compareTo(currentNode.value) < 0) {

                currentNode = currentNode.leftNode;


            //4. Traverse to the right if new item is less than the value of the current node
            } else {
                
                currentNode = currentNode.rightNode;
            }
        }

        //Insert the item as the correct child of the current node
        if (newItem.compareTo(currentNode.value) < 0) {
            currentNode.leftNode = newNode;

        } else {
            currentNode.rightNode = newNode;
        }

    }

    public void removeItem(String itemToRemove) {
        //Traverse items in tree until node to be removed is found
        Node currentNode = this.rootNode;
        Node previousNode = null;

        while (currentNode != null && currentNode.value != itemToRemove) {
            //Update previous node
            previousNode = currentNode;
            //Traverse to left if item to remove is less than current node's value
            if (itemToRemove.compareTo(currentNode.value) < 0) {
                currentNode = currentNode.leftNode;
            
            //Traverse to right if item to remove greater than current node's value
            } else {
                currentNode = currentNode.rightNode;
            }
        }
        //If the current node is null, the item to be deleted doesn't exist
        if (currentNode == null) {
            System.out.println("Item can't be deleted - does not exist");
        
        } else {
            //If the node to be deleted has no children...
            if (currentNode.leftNode == null && currentNode.rightNode == null) {
                //If the current node is less than the previous node, set the previous node's left pointer to null
                if (currentNode.value.compareTo(previousNode.value) < 0) {
                    previousNode.leftNode = null;

                //If the current node is greater than the previous node, set the previous node's right pointer to null    
                } else {
                    previousNode.rightNode = null;
                }
            }

            //If the node to be deleted has one child....
            else if (currentNode.leftNode == null || currentNode.rightNode == null) {
                //Find the child node
                Node childNode = null;
                if (currentNode.leftNode != null) {
                    childNode = currentNode.leftNode;
                
                } else {
                    childNode = currentNode.rightNode;
                }

                //If the current node is less than the previous node, set the previous node's left pointer to point to the child node
                if (currentNode.value.compareTo(previousNode.value) < 0) {
                    previousNode.leftNode = childNode;
                
                //If the current node is greater than the previous node, set the previous node's right pointer to point to the child node
                } else {
                    previousNode.rightNode = childNode;
                }
            
            //If the node to be deleted has 2 children, use the Hibbard deletion algorithm...
            } else {
                //Get the smallest node (the successor) in the right child's left subtree
                Node rightChild = currentNode.rightNode;

                Node smallestNode = rightChild;
                //Traverse to the left to get the smallest node
                while (smallestNode.leftNode != null) {
                    smallestNode = smallestNode.leftNode;
                }

                //Recursively remove the successor from the tree
                this.removeItem(smallestNode.value);

                //Set the value of the current node to be the value of the smallest node
                currentNode.value = smallestNode.value;

            }
        }
    }

    public void traversePreOrder(Node node) {
        //If this node can be traversed
        if (node != null) {
            //Output the data item at the root node of this subtree
            System.out.println(node.value);

            //Traverse the left subtree
            this.traversePreOrder(node.leftNode);

            //Traverse the right subtree
            this.traversePreOrder(node.rightNode);
        }
    }

    public void traverseInOrder(Node node) {
        //If this node can be traversed
        if (node != null) {
            //Traverse the left subtree
            this.traverseInOrder(node.leftNode);

            //Output the data item at the root node of this subtree
            System.out.println(node.value);

            //Traverse the right subtree
            this.traverseInOrder(node.rightNode);
        }
    }

    public void traversePostOrder(Node node) {
        //If this node can be traversed
        if (node != null) {
            //Traverse the left subtree
            this.traversePreOrder(node.leftNode);

            //Traverse the right subtree
            this.traversePreOrder(node.rightNode);

            //Output the data item at the root node of this subtree
            System.out.println(node.value);
        }
    }

    public static void main(String[] args) {
        Tree myTree = new Tree();

        myTree.addItem("Bob");
        myTree.addItem("Alice");
        myTree.addItem("Charlie");
        myTree.traverseInOrder(myTree.rootNode);
        myTree.removeItem("Bob");
        myTree.traversePreOrder(myTree.rootNode);
    }
}
