package com.oops.Inheritance;

public class User {

	public static void main(String[] args) {
		Guest g = new Guest();
		Developer dev = new Developer();
		Admin a = new Admin();
		System.out.println("Guest Class");
		g.read();
		System.out.println("Developer Class");
		dev.read();
		dev.write();
		System.out.println("Admin Class");
		a.read();
		a.write();
		a.manage();

	}

}
