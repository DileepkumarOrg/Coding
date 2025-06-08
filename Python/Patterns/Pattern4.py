n=5 #int(input())
"""for i in range(n,1,-1):
    print(" "*(i-1),"*"," "*,"*")
for i in range(n):
    print(" "*i,"*")
"""

for i in range(n):
    if i==0:
        print(" "*(n-i-1),"*")
    else:
        print(" "*(n-i-1),"*"," "*(2*i-2),"*")


"""for i in range(2*n):
    if i==0 or i==(2*n-1):
        for j in range(n-1):
            print(" ",end="")
        print("*")
    elif i==n:
        print("*",end="")
        for j in range(2*n-2):
            print(" ",end="")
        print("*")
    else:
        for i in range(n-2,0,-1):
            print(" ",end="")
        print("*")"""