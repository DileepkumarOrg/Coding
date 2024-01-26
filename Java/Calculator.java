//import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int loan_amount, choice, m, r, down_payment;
        
        System.out.print("Enter loan amount               : ");
        loan_amount = input.nextInt();
        
        System.out.print("Choose mode of Loan Term\n1.Monthly      2.Yearly         : ");
        choice = input.nextInt();
        
        if (choice == 1) {
            System.out.print("Enter Loan term (in Months)     : ");
            m = input.nextInt();
            
            System.out.print("Enter Interest Rate             : ");
            r = input.nextInt();
            
            System.out.print("Enter Amount paid(Down Payment) : ");
            down_payment = input.nextInt();
            
            month(loan_amount, m, r, down_payment);
        } else if (choice == 2) {
            System.out.print("Enter Loan term (in years)      : ");
            int t = input.nextInt();
            m = t * 12;
            
            System.out.print("Enter Interest Rate             : ");
            r = input.nextInt();
            
            System.out.print("Enter Amount paid(Down Payment) : ");
            down_payment = input.nextInt();
            
            month(loan_amount, m, r, down_payment);
        } else {
            System.out.println("Please Try again");
        }
    }
    
    public static void month(int loan_amount, int m, int r, int down_payment) {
        if (down_payment >= loan_amount) {
            System.out.println("Already paid Total amount");
        } else {
            int p = loan_amount - down_payment;
            double EMI = ((p * r / 1200) * Math.pow((1 + r / 1200), m) / (Math.pow((1 + r / 1200), m) - 1));
            System.out.println("Equated Monthly Instalment (EMI): " + Math.round(EMI));
            System.out.println("Interest Payable                : " + (int)(EMI * m - p));
            System.out.println("Total Payable amount            : " + (int)(EMI * m));
        }
    }
}