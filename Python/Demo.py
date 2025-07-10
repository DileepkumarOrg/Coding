"""class Dileep:
    def __init__(self, name, number, marks):
        self.name = name
        self.number = number
        self.marks = marks

s1 = Dileep("Dil",21, 45)
print(s1.number)
print(s1.name)
print(s1.marks)
print(2**7,'to',-2**7+1)"""



def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i ==0:
                return False
        return True
c = 0
for i in range(50,150):
    if isPrime(i):
        c += 1
        print(i)
print(c)
