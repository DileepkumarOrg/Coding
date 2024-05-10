n=5 #int(input(""))
for k in range((n + 1) // 2, 0, -1):
    print(end="-")
for i in range(1, n + 1, 2):
    for j in range(1,i+1):
        print(end="*")
    print("")