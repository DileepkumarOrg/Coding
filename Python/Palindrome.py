n="1234321"
n=list(n)
length=len(n)
for i in range(0,length//2):
    if n[i]==n[-(i+1)]:
        print("palindrome")
    else:
        print("not")