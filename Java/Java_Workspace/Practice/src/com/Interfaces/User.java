package com.Interfaces;

public class User{

	public static void main(String[] args) {
		Samsung s1 = new Samsung();
		Vivo v1 = new Vivo();
		s1.speakers();
		v1.speakers();
		s1.capture();
		v1.capture();
		s1.display();
		v1.display();
		s1.flash();
		v1.flash();
		s1.security();
		v1.security();
	}
}

