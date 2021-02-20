public class Stack {
    //Defined as private so the top variable can only be accessed by methods
    private Node top;

    public void push(String newData) {
        System.out.println("Pushing '" + String.valueOf(newData) + "' onto stack");
        //Create a new node object
        Node newEntry = new Node(newData);
        //Set the pointer of the node to the top of the list
        newEntry.pointer = top;
        //Set the top pointer to point to this new item
        top = newEntry;
    }

    public void pop() {
        //If top is a null object, display an error message
        if (top == null) {
            System.out.println("ERROR: stack is empty");
        }
        //Otherwise, set the value of the top variable to the node pointed to by it (the next item in the stack)
        else {
            System.out.println("Popping '" + readTop() + "' from stack");
            top = top.pointer;
        }
    }

    public Boolean isEmpty() {
        //If the value of top is null, the stack is empty
        if (top == null) {
            return true;
        }
        //Otherwise, it isn't empty
        else {
            return false;
        }
    }

    public String peek() {
        //If the stack is empty, the top variable cannot be read
        if (isEmpty()) {
            return "ERROR: stack is empty";
        }
        //Otherwise, return the data in the top variable
        else {
            //Return the data in the top variable
            return String.valueOf(top.data);
        }
    }
}
