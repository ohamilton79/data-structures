public class LinkedList {

    private Node top;

    //Methods to get and set the top pointer without directly accessing the variable (encapsulation)
    public Node getTop() {
        return top;
    }

    public void setTop(Node newTop) {
        top = newTop;
    }

    //Add a new item to the start of the linked list (assume that the data items are strings)
    public void addItem(String data) {
        //1. and 2. Create the new node
        Node newNode = new Node(data);
        //3. and 4. Get the node pointer to by the top pointer and set the address field of the new node as the top node
        newNode.pointer = getTop();

        //5. Get the top pointer to point to this new node
        setTop(newNode);
    }

    //Delete an item from the start of the linked list
    public void deleteTop() {
        //1. - Get the top variable
        Node topItem = top;

        //2. (Not needed for Java implementation - storage of objects in memory
        // is handled automatically

        //3. Get the item that will become the new first item in the list
        Node newTopItem = topItem.pointer;

        //4. Set the top variable to this new (first) item in the linked list
        top = newTopItem;
    }

    //Delete a specific value from the linked list
    public void deleteItem(String targetValue) {

        //1. If the item isn't in the linked list, output an error
        if (searchForNode(targetValue) == null) {
            System.out.println("ERROR: item couldn't be deleted - doesn't exist in list");
            return;
        }

        //Get the node associated with the value we are trying to delete
        Node nodeToRemove = searchForNode(targetValue);
        //Remove this node
        removeNode(nodeToRemove);
    }


    public void removeNode(Node nodeToRemove) {
        //2. If the item is at the start of the list, call our function to delete the top node
        if (nodeToRemove == top) {
            deleteTop();
        }

        //3. If the item is at the end of the list, overwrite the node with a null value
        if (nodeToRemove.pointer == null) {
            //Set this node as null (empty and can be overwritten)
            nodeToRemove = null;

        //4. If the item is in the middle of the list, search for the parent and re-assign its pointer
        } else {
            Node parentNode = searchForParent(nodeToRemove.data);
            //Set the pointer of the parent to the pointer of the node we want to remove
            //(i.e. 'skip out' the node to remove, so it's no longer in the list)
            parentNode.pointer = nodeToRemove.pointer;
        }
    }


    //Traverse the linked list and output each item
    public void traverse() {
        //1. Get the first item
        Node currentItem = top;

        //Repeat until the end of the list is reached
        while (currentItem != null) {
            //2. Retrieve and output the data stored
            System.out.println(currentItem.data);

            //3. Get the next new node from the address field of the current one
            currentItem = currentItem.pointer;
        }
    }

    //Search for a specific data item in the linked list and return its parent node
    // if it exists in the list
    public Node searchForParent(String targetData) {
        //1. Get the first item
        Node currentItem = top;

        //If the current item is null (the list is empty), the item doesn't exist in the list
        if (currentItem == null) {
            return null;
        }

        //If the data attribute of the top of the list is equal to the target item, return an empty node as it has no parent
        if (top.data.equals(targetData)) {
            return new Node(null);
        }

        //Whilst the end of the list hasn't been reached
        while (currentItem.pointer != null) {
            //2. If the data field of the child of this item is equal to the target data,
            // return this node (the parent of the child)
            if (currentItem.pointer.data.equals(targetData)) {
                return currentItem;
            }
            //3. Get the next new node from the address field of the current one
            currentItem = currentItem.pointer;
        }

        //5. If the while loop completes, and no value has been returned,
        // return null as the item doesn't exist in the linked list
        return null;
    }

    public Node searchForNode(String targetData) {
        //1. Get the first item
        Node currentItem = top;

        //If the current item is null (the list is empty), the item doesn't exist in the list
        if (currentItem == null) {
            return null;
        }

        //If the data attribute of the top of the list is equal to the target item, return the top node
        if (top.data.equals(targetData)) {
            return top;
        }

        //Whilst the end of the list hasn't been reached
        while (currentItem.pointer != null) {
            //2. If the data field of the child of this item is equal to the target data,
            // return the pointer of this node (the child node)
            if (currentItem.pointer.data.equals(targetData)) {
                return currentItem.pointer;
            }
            //3. Get the next new node from the address field of the current one
            currentItem = currentItem.pointer;
        }

        //5. If the while loop completes, and no value has been returned,
        // return null as the item doesn't exist in the linked list
        return null;
    }
}
