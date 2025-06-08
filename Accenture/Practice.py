res = []
n = int(input())
for n in range(n+1):
    if n>1:
        c=0
        for i in range(1,n//2+1):
            if n%i==0:
                c=c+1
        if c>1:
            print("not prime")
        else:
            res.append(n)
    else:
        print("Not a prime")

print(res)
