l=eval(input())
s1=9
l1=[]
for i in range(0,len(l)):
    s=s1-l[i]
    if s in l:
        l1.append(i)
        l1.append(l.index(s))
        print(l1)
        print(l[i],s)
        break



