"""d = {}
s = input()
s = s.replace(" ",'')
s1 = list(set(list(s)))
s1.sort()
print(s1)
for j in s1:
    c = 0
    for i in range(len(s)):
        if i == j:
            c+=1

    d[j]=c
print(d)"""

"""l = [1,2,3,4,5,6,7,8,9]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i:j])"""

"""s = "HACK"
s = list(s)
print(s)"""

"""
l = [21,6,5,12,56,45,32]

l = list(reversed(l))  
#l.sort(reverse=True)

print(l)"""



l = [21,6,5,12,56,45,32]
l = sorted(l,key = lambda x : x>12,l)
print(l)

