def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*(fact(n-1))


l=['Hello','World','Python']
n=[]
count=0
for i in l:
    for j in i:
        if j.isalpha() and j not in ['a','e','i','o','u']:
            count+=1
    n.append(count)
    count=0
print(fact(max(n)))