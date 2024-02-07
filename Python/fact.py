n=2
fact = 1
for i in range(1, n + 1):
    if n == 1:
        fact = 1
    else:
        fact = fact * i
print(fact)