package com.Practice;
import java.util.Scanner;
public class Bubble_Sorting {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter size of array : ");
		int size = s.nextInt();
		int[] arr = new int[size];
		for (int i = 0 ; i < size; i++) {
			System.out.printf("Enter arr[%d] = ", i);
			arr[i] = s.nextInt();
		}s.close();
		System.out.print("Before Sorting : ");
		for (int j : arr) {
			System.out.print(j+ " ");
		}
		System.out.println();
		System.out.print("After Sorting : ");
		for (int k = 0 ; k < size; k++) {
			for (int g = 0; g < size; g++) {
				if (arr[k] < arr[g]) {
					var temp = arr[k];
					arr[k] = arr[g];
					arr[g] = temp;
				}
			}
		}
		for (int u : arr) {
			System.out.print(u+" ");
		}
	}
}