def isPrime(n):
    if n<2:
        return False
    #elif n==2:
    #    return True
    else:
        for i in range(2,int(n**0.5+1)):
            if n%i==0:
                return False
        return True
for i in range(1,int(input("Enter N : "))):
    print(i,isPrime(i))