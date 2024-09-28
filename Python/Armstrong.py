n=int(input("Enter number: "))
p=1
while n>0:
    rem=n%10
    n=n//10
    rem=rem**3
    p=p*rem
if p==n:
    print("Strong")
else:
    print("No")

"""n=input("Enter value of n: ")
l=len(n)
count=1
for i in range(0,l):
    if n[-(i+1)] == n[i]:
        count=count+1
        if count==l:
            print("Armstrong")
        else:
            print("Not Armstrong")"""