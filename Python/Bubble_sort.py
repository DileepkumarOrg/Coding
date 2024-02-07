a=[9,5,8,6,2,3]
n=len(a)
print(n)
for j in range(n):
    for i in range(n-j-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            print(a)