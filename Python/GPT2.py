"""Task: Group Words by Their First Letter
Write a Python program that takes a list of words and groups them in a dictionary based on their first letter.
Input:
["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]

Output:
{
 'a': ['apple', 'avocado', 'apricot'],
 'b': ['banana', 'blueberry'],
 'c': ['cherry']
}"""

#Manully
l = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
#l2 = list(set((map(lambda x:x[0],l))))  --> [a,b,c]
l1 = sorted(l)+[" "]
print(l1)
l2 = []
d={}
l2.append(l1[0])
for i in range(1,len(l1)):
    if l1[i][0]==l1[i-1][0]:
        l2.append(l1[i])
    else:
        d[l1[i-1][0]]=l2
        l2=[]
        l2.append(l1[i])
print(d)


# From Chat GPT
from collections import defaultdict

l = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
d = defaultdict(list)

for word in l:
    d[word[0]].append(word)

# Optional: sort each group
d = dict(sorted((k, sorted(v)) for k, v in d.items()))
print(d)
