package com.Strings;

import java.util.Arrays;

// Intilaizaing Strings
// startWith
// endsWith
// contains
// equals
// equalsIgnoreCase
// length
// toUpperCase
// toLowerCase
// toCharArray
// trim (removing white spaces)
// indexOf
// lastIndexOf
// substring
// split
// charAt
// replace
// Integer.valueOf
// isEmpty
public class StringMethods {

	public static void main(String[] args) {
		String s1 = "This is a string";
		String s2 = new String("This is a string");
		System.out.println(s1 + " | " +s2);
		String s3 = "Object String";
		String s4 = new String("Object String");
		System.out.println(s1==s2);
		System.out.println(s1==s3);
		// equals
		System.out.println(s1.equals(s2));
		// startsWith
		System.out.println(s1.startsWith("Thi"));
		// endsWith
		System.out.println(s2.endsWith("ing"));
		// contains
		System.out.println("1" + s1.contains("is"));
		// equalsIngnoreCase
		String s5 = "THIS is A STRing";
		System.out.println(s1.equalsIgnoreCase(s5));
		System.out.println(s5.length());
		System.out.println(s5.toLowerCase());
		System.out.println(s5.toUpperCase());
		char[] array1 = s5.toCharArray();
		System.out.println(array1);
		System.out.println(s5.toCharArray());
		String s6 = "   Hello  World   ";
		System.out.println(s6.trim());
		System.out.println(s5.indexOf("S"));
		System.out.println(s5.lastIndexOf("S"));
		System.out.println(s5.substring(2,9));
		String[] s7 = s5.split(" ");
		for(int i = 0; i < s7.length; i++) {
			System.out.println(s7[i]);
		}
		System.out.println(Arrays.toString(s5.split(" ")));
		System.out.println(s5.charAt(5));
		System.out.println(s5.replace("i", "I"));
		String num = "456";
		System.out.println(Integer.valueOf(num));
		
		String s8 = "";
		System.out.println(s8.isEmpty());
	}

}
