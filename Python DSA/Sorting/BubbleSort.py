#   l = [8,7,5,2,6,9,7,5]
l = [6,6,2,4,8]
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)


l = [6,6,2,4,8]
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)

size = int(input("Enter size : "))
arr = []
for i in range(size):
    arr.append(int(input(f"Enter arr[{i}] : ")))
print(arr)
for i in range(size):
    for j in range(i,size):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)