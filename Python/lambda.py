"""x = lambda a: a+10
print(x(5))

y = lambda a,b: a+b
print(y(4,5))
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))"""

# map, lambda, list
l = ['2','3','4','12']
res = list(map(int,l))        #using map function to convert str into int
print(res)

res2 = list(map(lambda x: x*2, l))
print(res2)
res2 = list(map(lambda x: int(x)*2, l))
print(res2)

#Sorting Data using lambda

l = [5,6,4,2,3,-9,8]
l = sorted(l , key = lambda x: x*x)     #Using Based on squares so -9 is last
print(l)
l = [10,56,89,51,52]
l = sorted(l, key = lambda x: x%10)     #Sort the list based on digits place
print(l)
l = [("G7",9),('H8',2),('D4',7)]
l = sorted(l,key=lambda x: x[0][1])     #sort based on the Alphabet number
print(l)
l = sorted(l,key=lambda x: x[1])
print(l)

# using filter
l = [1,6,5,9,8,5]
res = filter(lambda x: x%2==0, l)
print(list(res))
res = filter(lambda x: x>5, l)
print(list(res))

#using reduce
import functools
l = [2,5,6,4,2,3]
res = functools.reduce(lambda x,y: x+y, l)
print(res)

# Summing of two lists
l1 = [1, 2, 3, 5]
l2 = [4, 5, 6]
res = map(lambda x, y : x+y, l1, l2)
print(list(res))

l1 = [2, 3, 4, 5, 6]
l2 = [4, 5, 6, 7, 8]

res = list(filter(lambda x: x[0] % 2 == 0 and x[1] % 2 == 0, zip(l1, l2)))
print(res)

#Task 7: Sort a list of strings based on the number of vowels in each string using lambda and sorted()
words = ["apple", "banana", "cherry", "kiwi", "grape"]
vowels = "aeiouAEIOU"
res = sorted(words, key= lambda x : sum(1 for i in x if i in vowels))
print(res)
res = sorted(words, key= lambda x: sum(1 for i in x if i not in vowels))
print(res)

#✅ Task 8: Use a lambda function with conditional logic inside map()
numbers = [12, 7, 9, 20, 15]
res= map(lambda x: "Even" if x%2==0 else "Odd", numbers)
print(list(res))

#✅ Task 9: Use lambda and filter() to keep only strings that contain at least one digit
l = ["apple1", "banana", "ch3rry", "kiwi", "grape9"]

print(all(map(lambda x: x.isalpha(), l)))

# Task 10 :  Use lamda to find max number
l = [1,2,3,4,5,9,8,5]
res = functools.reduce(lambda x,y: x if x>y else y, l)
print(res)

#Task 11 : Use Reduce and Lambda to find Duplicated elements
l = [1,2,5,6,5,4,2,5]
res = functools.reduce(lambda x,y: l.count(x)>l.count(y),l)
print(res)
