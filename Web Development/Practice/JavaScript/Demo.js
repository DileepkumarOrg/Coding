// Types of Variables
// var, let, constant
// Var: 
var a = "Apple"
console.log(a)  // Apple
a = "Dileep"
console.log(a)  // Dileep
var a = "Something"
console.log(a)  // Something

// let
let b = "Hello"
console.log(b)  // Hello

// let b = "Hello1"  // This will throw an error if uncommented

b = "Hello2"    // Hello2
console.log(b)

// Constant
const c = "Value1"
console.log(c)
//const c = "Value2"  // This will throw an error
//c = "Value3"  // This will throw an error
console.log(c)



// Auto Type Conversion
x = 10;
y = 20;
console.log(x + y);  // 30

// Practice on var
var x = 10;
var y = 20;
console.log(x+y);  // 30

// Practice on let
let p = 30; 
let q = 40;
console.log(p + q);  // 70

// Practice on const
const r = 50;
const s = 60;
console.log(r + s);  // 110


// Practice on var, let, const
var e = 70;  
let f = 80;  // Uncommenting this will throw an error if 't' is already declared with var or const
const g = 90;  // Uncommenting this will throw an error if 't' is already declared with var or let
console.log(e+f);  // 150
console.log(e+g);  // 160
// console.log(f+g);  // This will throw an error if uncommented, as 'f' is let and 'g' is const
// JavaScript is a dynamically typed language, meaning you don't need to declare the type of a variable when you create it. 
// Instead, the type is determined automatically based on the value assigned to the variable.

const price1 = 5;
const price2 = 6;
let total = price1 + price2;
console.log(total)  // 11


// DataTypes
/*  Primitive Data Types :  
                            String
                            Number
                            Boolean
                            Null
                            Undefined
    Complex Data Types:
                            Array
                            Object
*/

/*let num = "3" + (1 + 2);
console.log(num);        //33
let num1 = 3 + 1 + 2 + "3";
console.log(num1);       //63
let num2 = 3 + 1 + "2" + 3;
console.log(num2);       //4323 
let num3 = 3 + "1" + 2 + 3;
console.log(num3);       //3123 
let num4 = 3 + 1 + "2" + 3 + 4;
console.log(num4);       //31234
*/

let num = 10;
console.log(num<<=4)

console.log(typeof num)
const car = {type:"Fiat", model:"500", color:"white"};
console.log(car)
