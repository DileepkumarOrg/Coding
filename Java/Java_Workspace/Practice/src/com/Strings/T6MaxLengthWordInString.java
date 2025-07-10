package com.Strings;

public class T6MaxLengthWordInString {

	public static void main(String[] args) {
		String s = "Helloooooo Worldglkhngflkgjbndkjlgbdgnlibudl mjhfvjmhvnhfkuyjh";
		String[] s1 = s.split(" ");
		int max = 0;
		String maxStr = "";
		for (int i = 0; i < s1.length; i++) {
			if (s1[i].length() > max) {
				max = s1[i].length();
				maxStr = s1[i];
			}
		}System.out.println(maxStr);
	}
}
	