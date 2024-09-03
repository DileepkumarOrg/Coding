n=5
for i in range(n+1):
    for j in range(i):
        if i>=j:
            print(" ",end="")
        else:
            print("* ",end=" ")
    print(" ")