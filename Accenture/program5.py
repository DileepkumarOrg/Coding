"""61.

21

17

Maximize Pair Product

Noah is given an integer array A of length N. He must perform the
6following operations on the array:
. Select any integer pair/s from the array with their sum equal to
18

. From this select the pair with the maximum product such that the
first element of the pair is greater than the second element of the
pair.

Your task is to help Noah find and return a pair in the form of an integer
array which satisfies the conditions mentioned.

Input Specification:
input1 : An integer value N, representing the size of array A.
input2 : An integer array A.

Output Specification:

Return a pair in the form of an integer array which satisfies the
conditions mentioned.

Example 1:

input1 : 8
input2 : {11,1,2,8,10,11,15,7)

Output : (10,8)"""

n=int(input())
s=eval(input())
mx=1
for i in s:
    x=18-i
    if x in s:
        p=i*x
        if p>=mx:
            mx=p
for i in s:
    if mx%i==0:
        if mx//i in s:
            