// Calculating average of integer arrays

package com.Arrays;

import java.util.Scanner;

public class Task2AvgOfArrays {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter length of array : ");
		int len = s.nextInt();
		int a[] = new int[len];
		int i = 0;
		int avg = 0;
		while(i<len) {
			System.out.printf("Enter value of a[%d] : ",i);
			a[i] = s.nextInt();
			avg += a[i];
			i++;
			}
		System.out.println(avg/len);

	}

}
