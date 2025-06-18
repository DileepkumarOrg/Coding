package com.Practice;

import java.util.Scanner;

public class MarksIfElse {

	public static void main(String[] args) {
		System.out.println("Enter Marks : ");
		Scanner s = new Scanner(System.in);
		byte marks = s.nextByte();
		if (marks >= 35 && marks < 40) {
			System.out.println("Pass");
		}
		else if(marks >= 40 && marks < 50){
			System.out.println("B Grade");
		}
		else if(marks >= 50 && marks < 60) {
			System.out.println("A Grade");
		}
		else {
			System.out.println("Inavalid input ");
		}

	}

}
