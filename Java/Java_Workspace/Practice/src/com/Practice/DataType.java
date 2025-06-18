package com.Practice;

public class DataType {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte b = 45;
		short s = 128;
		int i = 989841651;
		long l = 456985645;
		System.out.println("Integer Group : "+"  " + b+"   "+  s +"    "+ i +"   "+ l );		// Integer Group :   45   128    989841651   456985645
		float f = 45.65f;
		double d = 45.6984653;
		System.out.println("Float Group : "+ f +"   "+ d);										// Float Group : 45.65   45.6984653
		char c = 'A' ;
		System.out.println("Char Group : "+"   "+ c);											// Char Group :    A
		boolean blen = true;
		System.out.println("Boolean Group : "+ "  "+blen);										// Boolean Group :   true
		System.out.println("Its time to find out size of Datatypes, by using SIZE keyword");
		System.out.println(Byte.SIZE/8+"  byte");								// 1 byte
		System.out.println(Short.SIZE/8+"  byte");								// 2 byte
		System.out.println(Integer.SIZE/8+"  byte");							// 4 byte
		System.out.println(Long.SIZE/8+"  byte");								// 8 byte
		System.out.println(Byte.MIN_VALUE+" to "+Byte.MAX_VALUE);				// -128 to 127
		System.out.println(Short.MIN_VALUE+" to "+Short.MAX_VALUE);				// -32768 to 32767
		System.out.println(Integer.MIN_VALUE+" to "+Integer.MAX_VALUE);			// -2147483648 to 2147483647
		System.out.println(Long.MIN_VALUE+" to "+Long.MAX_VALUE);				// -9223372036854775808 to 9223372036854775807
	}
}

