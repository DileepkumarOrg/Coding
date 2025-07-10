package com.Strings;

public class T4StringReverse {

	public static void main(String[] args) {
		String s = "Java is super";
		char[] c = s.toCharArray();
		for (int i = c.length - 1;i >= 0;  i--) {
			System.out.print(c[i]);
		}

	}

}
