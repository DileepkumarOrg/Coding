package com.Arrays;

public class Task6ReversingArray {

	public static void main(String[] args) {
		boolean[] b = new boolean[] {false,true,true,false,true};
		for (int i = b.length-1; i >= 0; i--) {
			System.out.print(b[i]+"  ");
		}

	}

}
