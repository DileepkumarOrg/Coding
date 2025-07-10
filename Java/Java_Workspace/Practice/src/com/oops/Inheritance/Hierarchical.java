package com.oops.Inheritance;

class Parent1{
	public void parent() {
		System.out.println("Parent class ");
	}
}

class Child1 extends Parent1{
	public void child1() {
		System.out.println("Child1 class");
	}
}

class Child2 extends Parent1{
	public void child2() {
		System.out.println("Child2 class");
	}
}

public class Hierarchical {

	public static void main(String[] args) {
		Child2 obj = new Child2();
		obj.child2();
		obj.parent();
		Child1 obj1 = new Child1();
		obj1.child1();
		obj1.parent();
	}
}



