n1=0
n2=1
n=int(input("Enter n : "))
if n>0:
    for i in range(n):
        n3=n1+n2
        n1=n2
        n2=n3
    print()