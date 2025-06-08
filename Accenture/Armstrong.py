n = int(input("Enter a number : "))
sum = 0
while n>0:
    n1=n%10
    n=n//10
    sum+=n1**3

if n == sum:
    print("Armstrong")
else:
    print("Not")