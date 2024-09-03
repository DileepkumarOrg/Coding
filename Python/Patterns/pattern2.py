n=5
for i in range(n):
    print(" ",end=" ")
    for j in range(n):
        if j>=i:
            print("*",end=" ")
        print()