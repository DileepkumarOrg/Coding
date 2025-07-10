package com.Strings;

public class EvenIndexStringWords {

	public static void main(String[] args) {
		String s = "Java is easy kevvu keva hello gfh jhgvku jhgvky kjhgvku jgkj gugkjy";
		String[] c = s.split(" ");
		for (int i = 0; i < c.length ;i++) {
			if (i%2 == 1) {
				System.out.print(c[i]+"  ");
			}
		}
	}

}

