input_values = map(int, input("").split())
n, a = input_values
n=n//2
for i in range(1,n+1):
    for j in range((n+1-i)*3):
        print("-",end="")
    for k in range(2*i-1):
        print(".|.",end="")
    for l in range((n+1-i)*3):
        print("-",end="")
    print("")
# WELCOME
for i in range((a-7)//2):
    print("-",end="")
print(end="WELCOME")
for i in range((a-7)//2):
    print("-",end="")
print("")

for i in range(n,0,-1):
    for j in range((n+1-i)*3):
        print("-",end="")
    for k in range(2*i-1):
        print(".|.",end="")
    for l in range((n+1-i)*3):
        print("-",end="")
    print("")