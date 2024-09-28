def IsPrime(n):
    c=0
    if n<=1:
        print("Not")
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                c=c+1
        if c==0:
            return n

l=eval(input("Enter ele: "))
l1=[]
for j in range(len(l)):
    if IsPrime(l[j]):
        l1.append(l[j])
print(sum(l1)-min(l1))