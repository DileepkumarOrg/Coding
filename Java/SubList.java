import java.util.ArrayList;
import java.util.List;

public class SubList {

    public static void main(String[] args) {
        // Create an ArrayList of integers
        List<Integer> numbers = new ArrayList<>();

        // Adding elements to the list
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        numbers.add(40);

        System.out.println("Original list: " + numbers);

        // Accessing elements by index
        int firstElement = numbers.get(0);
        System.out.println("First element: " + firstElement);

        // Updating an element
        numbers.set(1, 25);
        System.out.println("List after updating: " + numbers);

        // Removing an element
        numbers.remove(2);
        System.out.println("List after removing: " + numbers);

        // Checking if the list contains a specific element
        boolean containsElement = numbers.contains(30);
        System.out.println("Does the list contain 30? " + containsElement);

        // Getting the size of the list
        int size = numbers.size();
        System.out.println("Size of the list: " + size);

        // Iterating through the list
        System.out.print("List elements using for loop: ");
        for (int i = 0; i < numbers.size(); i++) {
            System.out.print(numbers.get(i) + " ");
        }
        System.out.println();

        // Clearing the list
        numbers.clear();
        System.out.println("List after clearing: " + numbers);
    }
}
