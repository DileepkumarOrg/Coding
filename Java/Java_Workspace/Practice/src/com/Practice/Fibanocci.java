package com.Practice;

import java.util.Scanner;

public class Fibanocci {
	public void fibanocci(int num) {
		if (num >= 1)
			System.out.print(0+" ");;
		if (num >= 2)
			System.out.print(1+" ");;
		int n1 = 0;
		int n2 = 1;
		if (num > 2) {
			for (int i = 0 ; i <= num-2; i++) {
				int n3 = n1+n2;
				n1 = n2;
				n2 = n3;
				System.out.print(n3+ " "); 
			}
		}
	}
	public static void main(String[] args) {
		Fibanocci fib =  new Fibanocci();
		Scanner s = new Scanner(System.in);
		System.out.println("Enter Number : ");
		int num = s.nextInt();
		fib.fibanocci(num);
	}
}
