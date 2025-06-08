#Code 1
def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                return False
        return True

n1 = int(input("Enter Number : "))
c = 0
n2 = 1
while c<n1:
    if isPrime(n2):
        n2+=1
        c+=1
    else:
        n2+=1
print(n2-1)

#Code 2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

print(nth_prime(n1))  # Example: 10th prime is 29
