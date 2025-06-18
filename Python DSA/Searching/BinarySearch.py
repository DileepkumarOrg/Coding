def isPresent(l,num):
    lower, upper = 0, len(l)-1
    while lower <= upper:
        mid = (lower + upper) // 2
        if l[mid] == num:
            return True
        elif l[mid] < num:
            lower = mid + 1
        else:
            upper = mid - 1
    return False

l = [5,4,6,9,8,1,2]
l.sort()            # [1, 2, 4, 5, 6, 7, 8, 9]
n = int(input("Enter number : "))
print(isPresent(l,n))

