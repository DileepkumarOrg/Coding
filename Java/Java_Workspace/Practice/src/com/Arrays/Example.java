package com.Arrays;

import java.util.Scanner;

public class Example {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int i[] = new int[5];
		//int[] j = new int[10];
		//int k[] = new int[] {1,2,3,4,5};
		int l[];
		l = new int[] {6,7,8,9};
		
		for(int a = 0; a <= i.length-1; a++) {
			System.out.printf("Enter element to the i[%d] = ",a);
			i[a] = s.nextInt();
		}
		s.close();
		int sum = 0;
		for (int j1 : i) {
			sum += j1;
		}
		System.out.println(sum);

	}

}
