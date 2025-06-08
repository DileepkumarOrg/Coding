def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                return False
    return True

n = int(input())
for i in range(n):
    n1 = int(input())
    l = []
    a = 2
    while n1 != 0:
        if isPrime(a):
            l.append(a)
            n1-=1
        a+=1
    print(l[::-1])
