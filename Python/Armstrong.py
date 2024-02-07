n=int(input("Enter number: "))
sum=0
while n>0:
    rem=n%10
    n=n//10
    #print(rem)
    fact = 1
    for i in range(1, rem + 1):
        if rem==1:
            fact=1
        else:
            fact = fact * i
    sum=sum+fact
if sum==n:
    print("Armstrong number")
else:
    print("Strong Number")