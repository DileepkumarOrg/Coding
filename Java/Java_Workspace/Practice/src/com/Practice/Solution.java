package com.Practice;

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = 5;
        for (int i = 0 ; i < n ; i++){
        	System.out.println("Enter number: ");
            int n1 = -150;
            System.out.println(n1 +" can be fitted in:");
            if (n1 > Byte.MIN_VALUE & n < Byte.MAX_VALUE){
                System.out.println("* "+ "byte");
            }
            if (n1 > Short.MIN_VALUE & n < Short.MAX_VALUE){
                System.out.println("* "+"short");
            }
            if (n1 > Integer.MIN_VALUE & n < Integer.MIN_VALUE){
                System.out.println("* "+"int");
            }
            if (n1 > Long.MIN_VALUE & n < Long.MAX_VALUE){
                System.out.println("* "+"long");
            }
            if (n1 >= Long.MAX_VALUE){
                System.out.println(n1+ "n can't be fitted anywhere.");
            }
        }
    }
}