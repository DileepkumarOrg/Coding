#n = list(map(str,input().split(" "))) Hello World 995 dileep 875 ,['Hello', 'World', '995', 'dileep', '875']
n = ['Hello', 'World', '995', 'dileep', '875']

def check(n):
    k=[]
    t=n
    while n>0:
        k.append(n%10)
        n=n//10
    if 9 not in k:
        return t

num= []
for i in n:
    if i.isdigit():
        num.append((int(i)))

for i in num:
    print(check(i))