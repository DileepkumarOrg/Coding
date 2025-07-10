package com.Arrays;

import java.util.Scanner;

public class Task4MaxNumber {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int max = 0;
		int maxIndex = 0;
		System.out.println("Enter length of Array : ");
		int len = s.nextInt(); s.nextLine();
		int a[] = new int[len];
		int i = 0;
		while (i < len) {
			System.out.printf("Enter a[%d] = ",i);
			a[i] = s.nextInt();
			i++;
		}
		for (int j = 0; j < len; j++) {
			if (a[j] > max) {
				max = a[j];
				maxIndex = j;
			}
		}
		System.out.println(max+" "+maxIndex);

	}

}
