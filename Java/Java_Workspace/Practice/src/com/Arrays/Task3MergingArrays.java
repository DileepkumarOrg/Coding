package com.Arrays;

import java.util.Scanner;

public class Task3MergingArrays {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter the array1 length : ");
		int len1 = s.nextInt();
		s.nextLine();
		String[] str = new String[len1];
		int i = 0;
		while(i < len1) {
			System.out.printf("Enter the value of str[%d] : ",i);
			str[i] = s.nextLine();
			i++;
		}
		System.out.println("Enter the array2 length : ");
		int len2 = s.nextInt();
		s.nextLine();
		String[] str2 = new String[len2];
		int i1 = 0;
		while(i1 < len2) {
			System.out.printf("Enter the value of str2[%d] : ", i1);
			str2[i1] = s.nextLine();
			i1++;
		}
		int finallen = len1+len2;
		String[] finalarray = new String[finallen];
		int i3 = 0;
		while (i3 < finallen) {
			if (i3<len1) {
				finalarray[i3] = str[i3];
			}
			else {
				finalarray[i3] = str[i3-len1];
			}
			i3++;
		}
		System.out.println(finalarray[0]+" "+finalarray[1]+" "+finalarray[2]+" "+finalarray[3]+" "+finalarray[4]);

	}
}
