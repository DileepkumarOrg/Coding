l = [6,5,3,1,8,7]
n = len(l)
for i in range(1,n):
    for j in range(i,0,-1):
        if l[j]<l[j-1]:
            l[j],l[j-1] = l[j-1],l[j]
print(l)    