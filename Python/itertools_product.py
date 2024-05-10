# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
input_values1 = list(map(int, input("").split()))
input_values2 = list(map(int, input("").split()))
if (len(input_values1)==3) & (len(input_values2)==1):
    print(list(product(input_values1, repeat=int(input_values2[0]))))
#print(list(product(input_values1, repeat=int(input_values2[0]))))
elif (len(input_values1)==3) & (len(input_values2)==2):
    print(list(product(input_values1, input_values2)))