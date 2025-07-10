package com.oops.Inheritance;


class Animal{
	public void Eating() {
		System.out.println("Eating");
	}
}

class Dog extends Animal{
	public void barking() {
		System.out.println("Barking");
	}
}

public class SingleLevel {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Dog obj = new Dog();
		obj.Eating();
		obj.barking();
	}

}
