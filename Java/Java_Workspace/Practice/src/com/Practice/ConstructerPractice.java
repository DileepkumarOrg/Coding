package com.Practice;

public class ConstructerPractice {
	int i;
	public static void main(String[] args) {
		ConstructerPractice cp = new ConstructerPractice();
		ConstructerPractice cp1 = new ConstructerPractice(34);
		System.out.println(cp.i);
		System.out.println(cp1.i);

	}
	
	public ConstructerPractice() {
		i = 20;
	}
	public ConstructerPractice(int a) {
		i = a;
	}

}
