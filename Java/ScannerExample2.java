import java.util.Scanner;

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
