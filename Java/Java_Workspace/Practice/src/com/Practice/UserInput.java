package com.Practice;

import java.util.Scanner;

public class UserInput {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter your Name: ");
		String firstName = s.nextLine();
		System.out.println(firstName);
		System.out.println("Enter your last name :");
		String lastName = s.next();
		System.out.println(lastName);
		System.out.println("Enter age: ");
		int age = s.nextInt();
		System.out.println(age);
		System.out.println("Are you single : ");
		boolean single = s.nextBoolean();
		System.out.println(single);
		System.out.println("marks : ");
		double marks = s.nextDouble();
		System.out.println(marks);
		System.out.println("contact Number : ");
		Long contact = s.nextLong();
		System.out.println(contact);
		

	}

}
