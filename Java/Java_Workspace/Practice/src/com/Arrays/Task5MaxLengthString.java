package com.Arrays;

public class Task5MaxLengthString {

	public static void main(String[] args) {
		String a[] = new String[] {"Office","Chai","HelloWorld...!","Ok"};
		String b[] = {"Hello","World","c"};
		int max = 0;
		String maxStr = null;
		int maxIndex = 0;
		for(int i = 0; i < a.length; i++) {
			if (a[i].length() > max) {
				maxStr = a[i]; maxIndex = i;max = a[i].length();
			}
		}
		System.out.println(maxStr+" "+maxIndex);
	}
}
