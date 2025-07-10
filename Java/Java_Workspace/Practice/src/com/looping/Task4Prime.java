package com.looping;

import java.util.Scanner;

public class Task4Prime {
	public static boolean isPrime(int num) {
		if (num < 2) {
			return false;
		}
		else {
			for (int i = 2; i < Math.sqrt(num)+1; i++) {
				//System.out.println(i);
				if (num % i == 0) {
					return false;
				}
			}
			return true;
		}
	}

	public static void main(String[] args) {
/*		Scanner s = new Scanner(System.in);
		Task4Prime t = new Task4Prime();
		System.out.println("Enter Number : ");
		int num = s.nextInt();
		System.out.println(t.isPrime(num));
		*/

		//Task4Prime t = new Task4Prime();
		int num = 50;
		int c = 0;
		while (num <= 150) {
			if (isPrime(num) == true) {
				System.out.println(num);
				c++;
			}
			num++;
		}
		System.out.println(c);
	}

}
