# Iterable
l = [1,2,3,4]
for i in range(len(l)):
    print(l[i])

# Iterator
iterator = iter(l)
print(iterator)
for i in range(len(l)):
    print(next(iterator))



