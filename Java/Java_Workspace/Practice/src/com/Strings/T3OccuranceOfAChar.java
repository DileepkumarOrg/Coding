package com.Strings;

import java.util.Scanner;

public class T3OccuranceOfAChar {

	public static void main(String[] args) {
		String s1 = "Hello World";
		char[] arr = s1.toCharArray();
		System.out.println("Enter character : ");
		Scanner s =new Scanner(System.in);
		char a = s.nextLine().charAt(0);
		int c =0;
		for (int i = 0; i<s1.length(); i++) {
			if (a == arr[i]) {
				c++;
			}
		}System.out.println(c);

	}

}
