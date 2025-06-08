"""def SumOfDigits(n):
    sum=0
    while(n>0):
        sum=sum+n%10
        n=n//10
    return sum


n=list(map(int,input().split()))
d={}
for i in n:
    y=SumOfDigits(i)
    if y not in d:
        d[i]=y
print(d.items())"""

l=[1,5,8,6]
l1=[]
mx=max(l)
mn=min(l)
print("{",mn,mx,"}")