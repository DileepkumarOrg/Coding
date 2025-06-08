"""Task: Build a Frequency Dictionary from a List of Words
Write a Python program that takes a list of words and builds a dictionary where each key is a word, 
and the corresponding value is the count of how many times that word appeared."""
# My approach
l = ["apple", "banana", "apple", "cherry", "banana", "apple"]
l1 = set(l)
d = {}
for i in l1:
    d[i]=l.count(i)
res =  sorted(d.items(), key = lambda x: x)
print(dict(res))

# Using Counter from collections
from collections import Counter
res = sorted(Counter(l).items(), key = lambda x: x[1], reverse= True)
print(dict(res))