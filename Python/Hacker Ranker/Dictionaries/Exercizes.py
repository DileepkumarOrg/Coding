d={
    "Model":2018,
    "Color":"Black",
    "Type":"Manual",
    "Brand":"Hundai"
}
"""print(d["Color"])
print(type(d))
print(d.get("Type"))
print(d.items())
print(d.keys())
print(d.values())
d["Color"]="White"
d.get("Color")
print(d.get("Color"))"""




"""print(d)
d["Model"]=2020
d.update({"Type":"Automatic"})
d["Seriol Number"]=24266546546
d["Ninja"]="Nuvve"
print(d)
del d["Ninja"]
print(d)
for i in d:
    print(i)
    print(d[i])
for j in d.values():
    print(j)
for k in d.keys():
    print(k)
for x,y in d.items():
    print(x,y)"""

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child1"].items())
for i in myfamily:
    for j in myfamily[i].items():
        print(j)