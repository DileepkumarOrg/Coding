a=[5,7,3,2,9]
n=len(a)
for i in range(n):
    temp=a[i]
    j=i-1
    while j>=0 and a[j]<temp:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp

print(a)