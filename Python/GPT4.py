"""li= eval(input())
l = [x**2 for x in li if x%2==0]
print(l)"""
"""nums = [1, 2, 3, 4]
words = ["one", "two", "three", "four"]
res = [(k,v) for k,v in zip(nums,words) if k%2==0]
print(res)

words = ["apple", "banana", "orange", "grape", "avocado"]
v = "aeiou"
res = [len(x) for x in words if x[0] in v]
print(res)

words = ["data1", "science", "py3thon", "hello", "abc123"]
res = [x for x in words if any(y.isdigit() for y in x)]
print(res)

res = [x for x in words if all(y.isalpha() for y in x) and len(x)>5]
print(res)

numbers = [11, 121, 1331, 22, 101, 12321, 123]
res = [i for i in numbers if str(i)==str(i)[::-1] and i%11==0]
print(res)

words = ["apple", "Banana", "sky", "crisp", "try", "orange"]
#words = eval(input())
res = [i for i in words if all(x.isalpha() for x in i) and len(i)>=5 if i[-1] in v]
print(res)

sentences = ["The sky is blue", "python is Fun", "I love programming"]
res = [i for j in sentences for i in j.split(" ") if i.islower() and len(i)>=4]
print(res)"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
"""coordinates = [[i, j, k] for i in range(x + 1) for j in range(y+1)for k in range(z + 1) if (i + j + k) != n]
print(coordinates)"""
coordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
print(coordinates)
