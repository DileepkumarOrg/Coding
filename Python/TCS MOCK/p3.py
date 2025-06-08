"""s="ssmmkksshhddbbkk"

def cnt(s,i):
    c=0
    for j in range(len(s)):
        if j==i:
            c+=1
    return c
l = []
for i in s:
    l.append(i)
b = set(l)
d={}
for i in range(len(b)):
    d(b[i])=cnt(s,i)
print(d)"""
d={}
l=['d','f','c']
l=set(l)
for i in range(len(l)):
    print(l[i])