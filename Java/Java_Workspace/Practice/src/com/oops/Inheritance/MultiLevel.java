package com.oops.Inheritance;

class GrnadParent{
	int i = 10;
	public void grnadParent() {
		System.out.println("GParent Method is working");
	}
}

class Parent extends GrnadParent{
	int j = 5;
	public void parent() {
		System.out.println("Parent Method is working");
	}
}

class Child extends Parent{
	int k = 1;
	public void child() {
		System.out.println("Child is Working");
	}
}

public class MultiLevel {

	public static void main(String[] args) {
		System.out.println("Child Class");
		Child obj = new Child();
		obj.child();
		System.out.println("Parent Class");
		System.out.println("k = "+obj.k);
		obj.parent();
		System.out.println("GrandParent Class");
		System.out.println("j = "+obj.j);
		obj.grnadParent();
		System.out.println("i = "+obj.i);

	}

}
