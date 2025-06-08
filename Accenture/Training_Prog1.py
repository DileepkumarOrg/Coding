"""Problem Statement:
You are given an array nums of integers and an integer k. Your task is to
rotate the array to the right by k steps. In a right rotation, each element
in the array moves to its right, and the last element wraps around to
the front of the array.

Write a Python function rotate(n, nums, k) that takes:

. An integer n, representing the number of elements in the array.
. A list of integers nums with n elements.
· An integer k, representing the number of steps to rotate the
array.

The function should modify the array in-place to rotate it by k steps.

Input Format:

. An integer n (1 ≤ nnn ≤ 100,000) - the number of elements in the
array.
. A list of integers nums of length n - the array to be rotated.
. A non-negative integer k - the number of steps to rotate the array.

Output Format:.
The function does not return anything but modifies the list nums in-place
to rotate it to the right by k steps. The updated array should be printed
after the rotation.

Input:

6

123456

2

Output: [5, 6, 1, 2, 3, 4]"""

def rotate(n,nums,k):
    for i in range(k):
        t=nums[-1]
        nums.remove(t)
        nums.insert(0,t)
    return nums



n=int(input())
nums=list(map(int,input().split()))
k=int(input())
print(rotate(n,nums,k))



