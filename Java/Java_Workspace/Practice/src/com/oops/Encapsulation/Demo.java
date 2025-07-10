package com.oops.Encapsulation;

// Step 1
/*class Human{
	int age = 30;
	String name = "Dileep";
}
public class Demo {

	public static void main(String[] args) {
		Human obj = new Human();
		System.out.println(obj.age);
		System.out.println(obj.name);
	}

} */

// Step 2
/*class Human{
	private int age = 30;
	private String name = "Dileep";
	
	public int getAge() {               		// Getters
		return age;
	}
	
	public String getName() {
		return name;
	}
}
public class Demo {

	public static void main(String[] args) {
		Human obj = new Human();
		System.out.println(obj.getAge());
		System.out.println(obj.getName());
	}

}*/

// Step 3 

class Human{
	private int age;
	private String name;
	
	public int getAge() {               		// Getters
		return age;
	}
	
	public String getName() {
		return name;
	}
	
	public void setAge(int a) {					// Setters
		age = a;
	}
	
	public void setName(String n) {
		name = n;
	}
}
public class Demo {

	public static void main(String[] args) {
		Human obj = new Human();
		obj.setAge(35);
		obj.setName("Dileep");
		System.out.println(obj.getAge());
		System.out.println(obj.getName());
	}

}