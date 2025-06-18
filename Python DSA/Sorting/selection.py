l = [9,5,4,8,6,2]
n = len(l)
for i in range(n):
    min = i
    for j in range(i+1,n):
        if l[j] > min:
            min = l[j]
    l[i],min = min,l[i]
print(l)
