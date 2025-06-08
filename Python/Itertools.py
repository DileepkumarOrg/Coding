import itertools
#Count
print("counter output : ")
counter = itertools.count(10,2)
l = []
for i in counter:
    l.append(i)
    if i==20:
        break
print(l)            #[10, 12, 14, 16, 18, 20]

#cycle
print("cycle Output : ")
l = ["A","B","C"]
cycler = itertools.cycle(l)
l1 = []
for i,j in enumerate(cycler,start=1):
    print(i,j,sep=":")
    if i==20:
        break
#repeat
"""s = "String"
repeater = itertools.repeat(s)
for i,j in enumerate(repeater,start=1):
    print(i,j)
    if i==20:
        break"""
#Accumulate
"""import operator
l = [1,2,3,4,5]
accumulater = itertools.accumulate(l,operator.mul)
print(list(accumulater))"""

#Factorial by using itertools
"""import operator
n = int(input("Number: "))
num = itertools.count(1)
l=[]
for i in num:
    l.append(i)
    if i==n:
        break
a = itertools.accumulate(l,operator.mul)
print(list(a)[-1])"""

#Chain --> To combine two lists
"""a = [1,2,3,6]
b = ["a","b","c","d"]
Combine = itertools.chain(a,b)
print(list(Combine))"""

#Compress
"""a = ["a","b","c","d"]
b = [1,0,1,0]
compressed = itertools.compress(a,b)
print(list(compressed))"""
