package com.Strings;

public class RepeatedNotRepeatedFirstLetter {

	public static void main(String[] args) {
		String s = "java is easy";
		char[] c = s.toCharArray();
		for (int i =0 ; i < c.length; i++) {
			if (s.indexOf(c[i]) != s.lastIndexOf(c[i])) {
				System.out.println("First repeated Letter is "+c[i]);
				break;
			}
				
		}
		for (int i =0 ; i < c.length; i++) {
			if (s.indexOf(c[i]) == s.lastIndexOf(c[i])) {
				System.out.println("First non repeated Letter is "+c[i]);
				break;
			}
				
		}

	}

}
