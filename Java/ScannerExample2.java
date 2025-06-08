/*import java.util.Scanner;

public class ScannerExample2 {
    public static void main(String args[]){
       Scanner obj = new Scanner(System.in);
       System.out.println("1.Addition \n 2.Subtraction\n 3.Multiplication \n 4.Division ");
       int chioce = obj.nextInt();
       System.out.print("Enter your number1: ");
       int num1 = obj.nextInt();
       System.out.print("Enter your number1: ");
       int num2 = obj.nextInt();
       if (chioce == 1){
            System.out.println(num1 + "+" + num2+ " = "+(num1+num2));
       }
       else if (chioce == 2){
            System.out.println(num1 + "-" + num2+ " = "+(num1-num2));
       }
       else if (chioce == 3){
            System.out.println(num1 + "x" + num2+ " = "+(num1*num2));
       }
       else if (chioce == 4){
            System.out.println(num1 + "/" + num2+ " = "+(num1/num2));
       }
       else{
        System.out.println("Invalid choice......!");
       }
    }
    
}
*/
import java.util.Scanner;

public class ScannerExample2 {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.println("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division ");
        System.out.print("Enter your choice: ");
        int choice = obj.nextInt(); // Fixed typo: 'chioce' -> 'choice'

        System.out.print("Enter your number1: ");
        int num1 = obj.nextInt();

        System.out.print("Enter your number2: "); // Fixed prompt: 'number1' -> 'number2'
        int num2 = obj.nextInt();

        // Perform operation based on choice
        switch (choice) {
            case 1:
                System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));
                break;
            case 2:
                System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
                break;
            case 3:
                System.out.println(num1 + " x " + num2 + " = " + (num1 * num2));
                break;
            case 4:
                if (num2 != 0) {
                    System.out.println(num1 + " / " + num2 + " = " + (num1 / num2));
                } else {
                    System.out.println("Division by zero is not allowed.");
                }
                break;
            default:
                System.out.println("Invalid choice!");
        }

        obj.close(); // Close the scanner
    }
}
