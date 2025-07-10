package com.Practice;

import java.util.Scanner;

public class SwitchCaseArthemetic {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter Number1 : ");
		double num1 = s.nextDouble();
		System.out.println("Enter Number2 : ");
		double num2 = s.nextDouble();
		System.out.println("Enter Arthematic Operation : ");
		char c = s.next().charAt(0);
		double res;
		switch(c) {
		case '+' :
			res = num1 + num2;
			System.out.println(res);
			break;
		case '-':
			res = num1 - num2;
			System.out.println(res);
			break;
		case '*':
			res = num1*num2;
			System.out.println(res);
			break;
		case '/':
			res = num1 / num2;
			System.out.println(res);
			break;
		case '%':
			res = num1 % num2;
			System.out.println(res);
			break;
		default :
			System.err.println("Invalid Input");
			
		}
		

	}

}
