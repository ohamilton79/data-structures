public class HashTableLinearProbing {
    private int size;
    private String[] tableArray;
    
    public HashTableLinearProbing(int size) {
        //Array to store hash table elements   
        this.tableArray = new String[size];

        //Define size of hash table
        this.size = size;
    }

    //Hash the string
    public int hash(String key) {
        //Calculate hash value based on sum of character codes
        int hashValue = key.chars().sum() % this.size;

        return hashValue;
    }

    //Add an item to the hash table
    public boolean add(String key) {
        //Calculate hash value
        int hashValue = hash(key);

        //Apply linear probing to insert item
        int currentIndex = hashValue;
        int count = 0;

        //While the item can't be inserted, and there are still array indices to check
        while (count != this.size && this.tableArray[currentIndex] != null) {
            //Re-hash
            currentIndex = (currentIndex + 1) % this.size;

            //Increment counter
            count++;
        }

        //If the item can be inserted at this location
        if (this.tableArray[currentIndex] == null) {
            //Insert the item
            System.out.println(String.format("Item '%s' added successfully to the hash table", key));
            this.tableArray[currentIndex] = key;
            return true;
        
        //Otherwise, there is no room in the hash table for the item
        } else {
            System.out.println(String.format("Item '%s' could not be added to the hash table", key));
            return false;
        }
    }

    //Search for an item in the hash table
    public boolean search(String searchItem) {
        //Calculate hash value to get table index
        int hashValue = hash(searchItem);

        //Apply linear probing to search for item
        int currentIndex = hashValue;
        int count = 0;

        //While the item isn't at this location, and there are still array indices to check
        while (count != this.size && this.tableArray[currentIndex] != searchItem) {
            //Re-hash
            currentIndex = (currentIndex + 1) % this.size;

            //Increment counter
            count++;
        }

        //If the item being searched for is at this location
        if (this.tableArray[currentIndex] == searchItem) {
            //Output that the item is in the hash table
            System.out.println(String.format("Item '%s' found in the hash table at index %d", searchItem, currentIndex));
            return true;

        //Otherwise, the item isn't in the hash table as all indices have been checked
        } else {
            System.out.println(String.format("Item '%s' not found in the hash table", searchItem));
            return false;
        }
    }

    //Traverse the hash table
    public void traverse() {
        //Output the value at each array index that isn't null
        for (int i = 0; i < this.tableArray.length; i++) {
            if (this.tableArray[i] != null) {
                System.out.println(this.tableArray[i]);
            }
        }
    }

    //Delete an item from the hash table
    public boolean delete(String itemToDelete) {
        //Calculate hash table index of item to delete
        int hashValue = hash(itemToDelete);

        //Apply linear probing to find item
        int currentIndex = hashValue;
        int count = 0;

        //While the item isn't at this location, and there are still array indices to check
        while (count != this.size && this.tableArray[currentIndex] != itemToDelete) {
            //Re-hash
            currentIndex = (currentIndex + 1) % this.size;

            //Increment counter
            count++;
        }

        //If the item to delete is at this location in the hash table
        if (this.tableArray[currentIndex] == itemToDelete) {
            //Delete the item
            System.out.println(String.format("Item '%s' successfully deleted from the hash table", itemToDelete));
            //Set the value at this array index to null, to represent the deletion of the item
            this.tableArray[currentIndex] = null;
            return true;

        //If the item to be deleted couldn't be found
        } else {
            //Output that the item couldn't be deleted
            System.out.println(String.format("Item '%s' could not be deleted from the hash table", itemToDelete));
            return false;
        }
    }

    public static void main(String[] args) {
        HashTableLinearProbing hashTable = new HashTableLinearProbing(31);
        hashTable.add("Jimmy");
        hashTable.add("John");
        hashTable.traverse();
        hashTable.search("Jimmy");
        hashTable.search("John");

        hashTable.delete("Jimmy");
        hashTable.traverse();

        hashTable.delete("Jack");
    }
}
