def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)
a = int(input("Enter tha value of N: "))
r = int(input("Enter the value of R: "))
if (r>0) & (r<a):
    sol = fact(a)//(fact(r)*fact(a-r))
else:
    print("Enter valid NCR ")