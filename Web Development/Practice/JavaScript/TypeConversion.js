var num = 55;
var str = "Hello";
console.log(num, typeof num);
console.log(str , typeof str);
num = String(num);
console.log(num, typeof num)
str = parseInt(num);
console.log(str,typeof(str))
str = parseFloat(num);
console.log(str,typeof str)

var floatNumber = 55.55555;
console.log(floatNumber, typeof floatNumber);                                       // 55.55555 number
floatNumber = parseFloat(floatNumber);                                              
console.log(floatNumber, typeof floatNumber);                                       // 55.55555 number
console.log(floatNumber.toExponential(), typeof floatNumber.toExponential())        // 5.555555e+1 string
console.log(floatNumber.toExponential(2), typeof floatNumber.toExponential(2))      // 5.56e+1 string
console.log(floatNumber.toFixed(), typeof floatNumber.toFixed())                    // 56 string
console.log(floatNumber.toFixed(2), typeof floatNumber.toFixed(2))                  // 55.56 string
console.log(floatNumber.toPrecision(), typeof floatNumber.toPrecision())            // 55.55555 string
console.log(floatNumber.toPrecision(2), typeof floatNumber.toPrecision(2))          // 56 string

var d = new Date();
Number(d)  
console.log(d,Number(d))                    // 2025-06-08T03:49:01.292Z 1749354541292

var d1 = Date();
Number(d1)  
console.log(d1,Number(d1))                  // Sun Jun 08 2025 09:19:01 GMT+0530 (India Standard Time)    NaN

var d2 = new getDate();
console.log(d2)
