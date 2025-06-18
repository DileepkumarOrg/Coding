package com.Practice;

public class Variables {
	static String staticVariable = "This is Static Variable.";
	String nonStaticVariable = "This is non static variable, by creating a object we can access.";

	public static void main(String[] args) {
		String localVariable = "This is local Variable.";
		Variables v1 = new Variables();
		System.out.println(localVariable);
		System.out.println(staticVariable);
		System.out.println(v1.nonStaticVariable);
		test("This is parameter variable.");
	}
	public static void test(String parameter){
			System.out.println(parameter); 
	}
}
