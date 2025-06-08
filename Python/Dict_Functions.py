# pop, copy, ID
"""users={0:"Dileep",1:"Sandeep",2:"Vasu",3:"Jaggu",4:"Shyam"}
print(users.keys())
print(users.values())
print(users.items())
poped = users.pop(3)
print(users,poped)
tocopy : dict =users.copy()
tocopy[2]="KJNl"
print(id(tocopy))
print(id(users))"""

#get()
"""users={0:"Dileep",1:"Sandeep",2:"Vasu",3:"Jaggu",4:"Shyam"}
print(users)
print(users[3])
print(users.get(3))
print(users.get(5))
print(users.get(5,"Missing..!"))"""

# setdefault()
"""users={0:"Dileep",1:"Sandeep",2:"Vasu",3:"Jaggu",4:"Shyam"}
print(users)
print(users.setdefault(0,"????"))
print(users.setdefault(9,"????"))
print(users)"""

# clear()
"""users={0:"Dileep",1:"Sandeep",2:"Vasu",3:"Jaggu",4:"Shyam"}
print(users)
users.clear()
print(users)"""

# fromkeys()
"""user = ["Dileep","Sandeep","JHBIUK"]
people =  dict.fromkeys(user)
print(people)
people2 = dict.fromkeys(user,__value="Unknown")
print(people2)"""

# Alphabet Frequency
"""s="brontosaurus"
s1 = set(s)
s1 = list(s1)
s1.sort()
d={}
def c(n):
    t=0
    for i in range(len(s)):
        if s[i]==n:
            t+=1
    return t
for i in range(len(s1)):
    d.update({s1[i]:c(s1[i])})

for k,v in d.items():
    print(k,v)"""


d={'a': 1, 'b': 1, 'n': 1, 'o': 2, 'r': 2, 's': 2, 't': 1, 'u': 2}
print(sum(d.values()))