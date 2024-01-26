a=[2,5,4,6,3]
n=len(a)
print(n)
#print(a[0])
for i in range(0,n,1):
    if (a[i]<a[i+1]):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
    else:
        continue