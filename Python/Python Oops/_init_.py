class Employee:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
E1 = Employee("Dileep",22,20568)
print(E1.name)
print(E1.number)
print(E1.number)

for i in range(10):
    if i == 6:
        continue
    print(i)

x = (1,2,3,6,5)
print(x, x[::-1])

d = {"A":1,"B":2,"C":3}
print(d)

s = {1,2,3,6,54}
#print(s, s[::-1])



import random
l = [1,5,6,9,8,5]
s = ["DIleep", "kkj", "jknkjn"]
l = random.shuffle(l)
print(l)
print(random.randint(5,9))
print(random.choice(s))
print(random.random())
print()

