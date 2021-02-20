public class Queue {

    //Reference to the front of the queue
    Node head = null;
    //Reference to back of queue
    Node tail = null;


    public void push(String data) {
        System.out.println("Pushing...");
        //Create a new Node
        Node newItem = new Node(data);

        //If the tail isn't null, the previous tail in the queue now points to this
        if (tail != null) {
            tail.pointer = newItem;

        }
        //This is now the new 'tail' of the queue
        tail = newItem;

        //If the head is empty, this is also the new head of the queue
        if (head == null) {
            head = newItem;
        }
    }

    public void pop() {
        System.out.println("Popping...");
        //If the head variable is null, output an error message
        if (head == null)  {
            System.out.println("Error: Queue is empty");
        }
        else {
            //Otherwise, the head variable is now equal to the node that the previous head pointed to, as items are removed from the front
            head = head.pointer;
        }
    }

    public String readTop() {
        System.out.println("Getting item at the front of the queue");
        //If the value of the head variable is null (the queue is empty), return an error message
        if (head == null) {
            return "Error: Queue is empty";
        }
        //Otherwise, return the value of the node at the head of the queue
        else {
            return String.valueOf(head.data);
        }
    }

    public Boolean IsEmpty() {
        if (head == null | tail == null) {
            return true;
        }
        //Otherwise, it isn't empty
        else {
            return false;
        }
    }
}
