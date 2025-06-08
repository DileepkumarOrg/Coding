n = int(input())
a = eval(input())
a =
res=[]
def issqrt(n):
    n = n**0.5
    if n.is_integer():
        res.append(n)
for i in range(n):
    issqrt(a[i])
print(res)
