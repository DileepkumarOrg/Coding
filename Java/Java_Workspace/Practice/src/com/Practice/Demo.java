package com.Practice;

import java.util.Scanner;

public class Demo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		for (int i = 0; i <= 3; i++) {
			String str = s.nextLine();
			System.out.println("Enter Number: ");
			int num = s.nextInt();
			s.nextLine();
			System.out.println(num + "  ".repeat(15)+str);
		}

	}

}
