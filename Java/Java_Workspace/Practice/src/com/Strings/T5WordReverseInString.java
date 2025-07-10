package com.Strings;

public class T5WordReverseInString {

	public static void main(String[] args) {
		String s = "Java is super";
		String[] s1 = s.split(" ");
		for (int i = 0; i< s1.length;i++) {
			char[] c = s1[i].toCharArray();
			for (int j = s1[i].length()-1; j>=0 ;j--) {
				System.out.print(c[j]);
			}System.out.print(" ");
		}

	}

}
