public class Node {

    String value;
    Node leftNode = null;
    Node rightNode = null;

    public Node(String value) {
        this.value = value;
    }

    /*public Tree getTree() {
        //Create a new tree, with this node as the root
        Tree newTree = new Tree();
        newTree.rootNode = this;
        return newTree;
    }*/

    //Check if there is space for a new item to be inserted as the child of this node
    public boolean spaceAvailable(String newItem) {
        //If there is space to the left of this node, and the item to be added is less than this node's value
        if (this.leftNode == null && newItem.compareTo(this.value) < 0) {
            return true;
        }

        //If there is space to the right of this node, and the item to be added is greater than this node's value
        else if (this.rightNode == null && newItem.compareTo(this.value) >= 0) {
            return true;
        }

        else {
            return false;
        }
    }

    //Check if the data item of one node is later in the alphabet than another
    /*public boolean greaterThan(Node comparisonNode) {
        //Convert both of the data strings to character arrays
        char[] currentCharList = this.data.toCharArray();
        char[] comparisonCharList = comparisonNode.data.toCharArray();

        //Get the first characters
        char currentChar;
        char comparisonChar;

        //Counter variable
        int count = 0;
        //While there are still characters to check
        while (count < currentCharList.length - 1 && count < comparisonCharList.length - 1) {

            currentChar = currentCharList[count];
            comparisonChar = comparisonCharList[count];

            //Compare the first characters in each list
            if (currentCharList[0] > comparisonCharList[0]) {
                return true;
            }

            else if (currentCharList[0] < comparisonCharList[0]) {
                return false;
            }
            //Increment the counter
            count++;
        }

        //If execution reaches this point, the two strings have the same characters, so just return the longer string
        if (this.data.length() > comparisonNode.data.length()) {
            return true;
        }
            return false;
    }*/
}
