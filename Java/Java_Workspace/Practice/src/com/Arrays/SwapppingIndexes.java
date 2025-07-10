package com.Arrays;

public class SwapppingIndexes {

	public static void main(String[] args) {
		int arr[][] = {
				{1,2,1},
				{9,7,2},
				{7,6,4}
		};
		int arr2[][] = new int[arr[1].length][arr[1].length];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				arr2[j][i] = arr[i][j];
			}
		}
		for (int i = 0; i < arr2.length; i++) {
			for (int j = 0; j < arr2[i].length; j++) {
				System.out.print(arr2[i][j]+" ");;
			}System.out.println();
		}
		

	}

}
