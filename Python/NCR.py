def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)
a = int(input("Enter tha value of N: "))
r = int(input("Enter the value of R: "))
if (r>0) & (r<a):
    num=fact(a)
    den=(fact(r)*fact(a - r))
    sol = num//den
else:
    print("Enter valid NCR ")