def isPresent(l, num):
    for i in range(len(l)):
        if num == l[i]:
            return True
    return False
l = [4,2,6,8,5,9]
n = 8
print(isPresent(l,n))
