package com.Practice;

public class ObjPractice {
	
	int i,j;

	public ObjPractice() {
		i = 2;
		j = 3;
	}
	public ObjPractice(int i, int j) {
		this.i = i;
		this.j = j;
	}

	public static void main(String[] args) {
		ObjPractice op1 = new ObjPractice();
		ObjPractice op2 = new ObjPractice(3,4);
		ObjPractice op3 = new ObjPractice(4,5);
		System.out.println(op1.add());
		System.out.println(op2.add());
		System.out.println(op3.add());
	}
	public int add() {
		return i+j;
	}

}
