"""Dariel has a ball. He wants to find the ball's rebound height, which he dropped from height
6H with an initial velocity V. After the Nt rehound the final velocity of the ball is V. Your task is
to help bim find and return an integer value representing the height to which the ball rebounds
after N bounces.

Nate

. H' = Hxen, where H' is the rebound height, H is the initial height, e is the coefficient of restitution and is
the number of bounces.

en = V/Vn. where V is the initial velocity and Va is the final velocity

Input Specification:

input1 : An integer H, representing initial height
input2 : An integer V, representing initial velocity
input3 : An integer V., representing final velocity

Output Specification:

Return an integer value representing the height to which the ball rebounds after N bounces."""

def rebound(h,Vi,vf):
    x=(Vi/vf)**2
    return h*x

h=int(input())
Vi=int(input())
vf=int(input())
print(rebound(h,Vi,vf))