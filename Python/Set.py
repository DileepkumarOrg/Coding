set1 = {1,True,10,10,"Dileep"}
print(set1)
set2 = {}
print(type(set2))       #dictionary
set2 = set()
print(type(set2))       #set
set1.add("Hello")
print(set1)
set1.remove("Dileep")
print(set1)
set1.discard("Hello")
print(set1)
"""
The differenses between remove and discard, when you are trying to remove element which is not in the set it will show error
but discord never show any error.
"""
"""set1.remove(52)
print(set1)"""
#Traceback (most recent call last):
#  File "D:\Upload Git\Coding\Python\Set.py", line 17, in <module>
#    set1.remove(52)
#KeyError: 52

set1.discard(52)
print(set1)


set1 = {'A','B','C'}
set2 = {'C','D','E'}
set3 = {'D','B','G'}
print(set1.union(set2))         #{'B', 'E', 'D', 'A', 'C'}
print(set1.union(set2,set3))    #{'B', 'A', 'E', 'D', 'G', 'C'}
print(set1 | set2 | set3)       #{'B', 'A', 'E', 'C', 'G', 'D'}
print(set1.union(('X','Y')))    #{'C', 'X', 'Y', 'B', 'A'}
print(set1.union(['X','Y']))    #{'C', 'X', 'Y', 'B', 'A'}
set4 = {'A','D'}
set4.clear()
print(set4)
print(set4.issubset(set1))


# Hacker rank pbm
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 45, 78, 84, 23}
n = 2
l = [{1, 2, 3, 4, 5, 6},{100, 11, 12}]
print(all(map(lambda x:x.issubset(set1),l)))

# hacker Ranker pbm2
"""set1 = {2,4,5,9}
n1,n2 = 4,4
set2 = {2,4,11,12}
for i in range(n1):
    if set2(i).issubset(set1):
        set2.remove(set2(i))
        set1.remove(set2(i))
print(set1,set2)
for i in set1:
    print(i)"""

# Set operations

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))          # {4, 5}
print(set1.difference(set2))            # {1, 2, 3}
print(set1.difference_update(set2))
print(set1.isdisjoint(set2))            # True
print(set1.issuperset(set2))            # False
print(set1.symmetric_difference(set2))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.symmetric_difference_update(set2))