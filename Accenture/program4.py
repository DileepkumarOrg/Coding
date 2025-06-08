"""Sum XOR

You are given an array A of length N. Your task is to find and retum an
finteger value representing the difference between the sum of elements
at odd index and XOR of elements at even index.

Input Specification:
input1 : An integer N, representing the length of array
1a Input2 : An integer array A

Output Specification:
Retum an integer value representing the difference between the sum
of elements at odd index and XOR of elements at even index.

Example 1:

input1 : 6
input2 : (10,5,6,3,7,2)

Output : -1

Explanation:
Here N is 6 and the array A = [10,5,6,3,7,2}. The sum of elements at odd
positions are 5 + 3 + 2 = 10 and the XOR of elements at even positions
are 10 e6 e7 = 11 and the difference is 10 - 11 = -1. Therefore, -1 is
returned as the output."""


n=int(input())
s=eval(input())
sum=0
xor=0
for i in range(1,n,2):
    sum=sum+s[i]
for j in range(0,n,2):
    xor=xor^s[j]
print(sum-xor)