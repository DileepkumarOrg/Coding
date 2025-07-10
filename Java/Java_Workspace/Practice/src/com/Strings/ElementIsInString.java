package com.Strings;

public class ElementIsInString {

	public static void main(String[] args) {
		String input1 = "New York";
		String input2 = "NWYR";
		char[] c = input1.toCharArray();
		
		//Character.toLowerCase(c[i])
		/*for (int i = 0 ; i< c.length; i++) {
			if ((input2.indexOf(Character.toLowerCase(c[i])) != -1) || (input2.indexOf(Character.toUpperCase(c[i])) != -1)){
				System.out.print(c[i]+"+");
			}
		}*/
		//
		for (int i = 0 ; i< c.length; i++) {
			if ((input2.toLowerCase().indexOf(c[i]) != -1) || (input2.toUpperCase().indexOf((c[i])) != -1))
			{
				System.out.print(c[i]+"+");
			}
		
		}
	}
}



