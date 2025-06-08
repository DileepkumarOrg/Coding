numbers = [1,2,3,4,5,6]
strings = ["List","Comprehensions","GPT1","prime"]

"""
#Traditional
res = []
for i in numbers:
    i = i*2
    res.append(i)
print(res)

#Comprehension

res1 = [i*2 for i in numbers]
print(res1)"""


"""
#Tradional
res = []
for i in strings:
    i = i.upper()
    res.append(i)
print(res)

#Comp
res1 = [i.upper() for i in strings]
print(res1)
res2 = [i.upper()+"Dileep" for i in strings]
print(res2)"""


# With Func and if else

"""def timesSix(n):
    return n*6

res = [timesSix(i) if numbers.index(i) % 2 == 0 else i for i in [1, 2, 3, 6, 5, 4]]
print(res)
"""

#Range Function

"""l = [i for i in range(2,10+1,2)]
print(l)
"""

#List Comp for Dictionaries
"""dicts = [{"Name":"Mustang","Brand":"Ford"},{"Name":"Amaz","Brand":"Honda"}]
l = [(i["Name"], i["Brand"]) for i in dicts]
print(l)
"""

#Nested if
"""print(numbers)
l = [i*2 if i%2==0 else i for i in numbers]
print(l)
l = [i*2 if i%2==0 else i for i in numbers if i>3]
print(l)

#By using Lambda
l = map(lambda x: x*2 if x%2==0 else x, numbers)
print(list(l))
l = map(lambda x:x*2 if x%2==0 else x, filter(lambda x: x>3 ,numbers))
print(list(l))
    """

#Nested Loops in List Comprehension
l = [(i,j) for i in range(1,3) for j in range(1,3)]
print(l)        #Output : [(1, 1), (1, 2), (2, 1), (2, 2)]

matrix = [[1, 2], [3, 4]]
l = [i for j in matrix for i in j]
print(l)        # Output : [1, 2, 3, 4]

table = [[i*j for i in range(1,6)] for j in range(1,6)]
print(table)        #[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

#Dictionary Comprehensions
d = {"Die":5,"San":6,"asp":2,"owl":4}
res = {k:v for k,v in {1:2,2:3,3:4}.items()}
print(res)      #{1: 2, 2: 3, 3: 4}
res = {k:k**2 for k in range(1,11)}
print(res)      #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
res = {k:k**3 for k in range(1,6)}
print(res)      #{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
res = {k:len(k) for k in ["String","Chat","Comprehension"]}
print(res)      #{'String': 6, 'Chat': 4, 'Comprehension': 13}
"""res = {k:v for k,v in d.items() if d.keys()[0][0] in "aeiouAEIOU" }
print(res)"""

s = "aabjfbkjnkjnkjfnalffnal"
res = [{x:s.count(x)} for x in set(s)]      #[{'k': 3}, {'f': 4}, {'a': 4}, {'b': 2}, {'j': 4}, {'n': 4}, {'l': 2}]
res = sorted(res, key= lambda x: a)