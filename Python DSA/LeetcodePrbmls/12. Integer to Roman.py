def intToRoman(num):
    numbers = [1000, 900, 500, 400, 200, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "CC", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_numerals = ""
    #i = 0
    while num > 0:
        for _ in range(len(numbers)):
            if num >= numbers[_]:
                roman_numerals += roman[_]
                num -= numbers[_]

        """for _ in range(num//numbers[i]):
            roman_numerals = roman_numerals + roman[i]
            num = num - numbers[i]"""
        #i += 1
    return roman_numerals




print(intToRoman(97))



#d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}