"""def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a//b)
n=int(input())
arr=list(map(int,input().split()))
smallest=min(arr)
largest=max(arr)
print(gcd(smallest,largest))"""


s=list(map(int,input().split("'")))
print(s)