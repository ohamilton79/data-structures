import java.util.*;

public class HashTableChaining {
    int size;
    //Array to store elements of hash table
    List<LinkedList<String>> tableArray = new ArrayList<LinkedList<String>>();

    //Constructor
    public HashTableChaining(int size) {
        this.size = size;

        //Add linked lists to each array index
        for (int i=0; i < size; i++) {
            tableArray.add(new LinkedList<String>());
        }
    }

    public int hash(String key) {
        int modulus = key.chars().sum() % size;
        return modulus;
    }

    public void add(String key) {
        //1. Get the hash value
        int hashValue = hash(key);

        //2. Add the key to the existing linked list
        tableArray.get(hashValue).add(key);
    }

    public void traverse() {
        //Traverse each linked list in the hash table
        for (LinkedList<String> linkedList : tableArray) {
            if (linkedList != null) {
                //Traverse linked list
                ListIterator<String> listIterator = linkedList.listIterator();
                while (listIterator.hasNext()) {
                    System.out.println(listIterator.next());
                }
            }
        }
    }

    //Delete an item from the hash table
    public void delete(String key) {
        //1. Get the hash value
        int hashValue = hash(key);

        //2. Try to delete the item from the linked list at this location
        tableArray.get(hashValue).remove(key);
    }

    public static void main(String[] args) {
        HashTableChaining hashTable = new HashTableChaining(31);
        hashTable.add("John");
        hashTable.add("Mary");
        hashTable.delete("John");
        hashTable.traverse();
    }
}
