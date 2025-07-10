package com.Arrays;

import java.util.Arrays;

public class SpliStringIntoArray {

	public static void main(String[] args) {
		String s = "Hello World Hello Chinnu";
		System.out.println(Arrays.toString(s.split(" ")));				// [Hello, World, Hello, Chinnu]
		String s2 = "Hello^chinnu^Hel world";
		System.out.println(Arrays.toString(s2.split(" ^ ")));			// [Hello^chinnu^Hel world]
		System.out.println(Arrays.toString(s2.split("//^")));
	}

}
