package com.Practice;

public class methodsBank {
	static int currentBalance = 1000;
	public static void greet() {
		System.out.println("Hii Good Morning ..... !");
	}
	public void diposit(int amount) {
		currentBalance += amount;
		System.out.println("Amount diposited Successfully");
	}
	public static void withdrawl(int amount) {
		currentBalance -= amount;
		System.out.println("Amount withdrawl.");
	}
	public int getCurrentBalance() {
		return currentBalance;
	}

	public static void main(String[] args) {
		methodsBank  mb1 = new methodsBank();
		greet();
		System.out.println(mb1.getCurrentBalance());
		mb1.diposit(1000);
		System.out.println(mb1.getCurrentBalance());
		withdrawl(500);
		System.out.println(mb1.getCurrentBalance());
	}

}
