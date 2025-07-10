// Print the sum of array integers
package com.Arrays;

import java.util.Scanner;

public class Task1SumOfArrays {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int sum = 0;
		System.out.println("Enter length of the Array : ");
		int len = s.nextInt();
		int[] a = new int[len];
		for (int i = 0; i <= len-1; i++) {
			System.out.printf("Enter value of a[%d] : ",i);
			a[i] = s.nextInt();
			sum += a[i];
		}
		System.out.println(sum);
		
		
		

	}

}
