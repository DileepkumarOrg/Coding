package com.Arrays;

public class TwoDimensionalArrayMatchElements {

	public static void main(String[] args) {
		int arr[][] = {
				{1,2,1},
				{9,7,2},
				{7,6,4}
		};
		int arr2[][] = {
				{2,6,8,4},
				{0,1,3,9,7},
				{7,2,0},
				{8,3}
		};
		for(int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				for (int k = 0; k< arr2.length; k++) {
					for (int l = 0; l < arr2[k].length ; l++) {
						if (arr[i][j] == arr2[k][l]) {
							System.out.print(arr[i][j]+"  ");
						}
					}
				}
			}
		}

	}

}
