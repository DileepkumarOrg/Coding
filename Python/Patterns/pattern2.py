"""
for i in range(n):
    for j in range(i):
        print(end="* ")
    print()


Output:
*
* *
* * *
* * * *
* * * * * """

"""
n=5
for i in range(n):
    for j in range(n):
        if i==j:
            print(end="* ")
        else:
            print(end="   ")
    print(
        
        
*             
   *          
      *       
         *    
            * 
"""


n=5
for i in range(n,0,-2):
    for j in range(i):
        for k in range(n//2):
            print(end="  ")
        print(end="* ")
    print()