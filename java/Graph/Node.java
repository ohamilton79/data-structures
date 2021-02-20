package src;

public class Node {

    String value;
    String[] connectedVertices;

    public Node(String value, String[] connectedVertices) {
        this.value = value;
        this.connectedVertices = connectedVertices;
    }
}
