x=[1,2,3,4,5,6]
h=[1,2,3,4]
y=[]
m=len(x)
n=len(h)
if m-n!=0:
    if m>n:
        for i in range(0,m-n):
            h.append(0)
        print(h)
    elif n>m:
        for i in range(0,n-m):
            x.append(0)
        print(x)

