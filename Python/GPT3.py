#🧪 Task: Filter and Square Even Numbers Only

l = [1, 2, 3, 4, 5, 6]
res2 = map(lambda x:x**2 ,filter(lambda x:x%2==0,l))
print(list(res2))