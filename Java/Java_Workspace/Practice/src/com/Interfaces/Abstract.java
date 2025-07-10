package com.Interfaces;

public abstract class Abstract implements Mobile{
	public void display() {
		System.out.println("Abstract display code.");
	}
	
	public void speakers() {
		System.out.println("Abstract speakers code.");
	}
	
	public void flash() {
		System.out.println("Abstract flash code.");
	}
	
	public abstract void  capture();
	public abstract void software();
	public abstract void security();
}


