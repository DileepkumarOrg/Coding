package com.Strings;

import java.util.Scanner;

public class T7FirstLastNames {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		System.out.println("Enter First Name : ");
		String firstName =  s.nextLine();
		System.out.println("Enter Last Name : ");
		String lastName = s.nextLine();
		System.out.println(lastName+","+firstName.charAt(0));

	}

}
