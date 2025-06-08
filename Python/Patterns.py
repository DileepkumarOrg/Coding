def square(n):
    for i in range(n):
        print("* "*n)

def pattern1(n):
    print("Pttern1")
    for i in range(1,n+1):
        print("* "*i)
def pattern2(n):
    print("Pattern2")
    for i in range(n,0,-1): #for i in range(1,n+1):
        print("* "*i)            #print("* "*(n+1-i))

def pattern1and2(n):
    print("Pattern1 & Pattern2")
    for i in range(1,n):
        print("* "*i)
    for j in range(1,n+1):
        print("* "*(n+1-j))

def pattern3(n):
    for i in range(1,n+1):
        print(" "*((n-i)*2-1),end="")
        print(" *"*i)
    #for j in range()



def hollowRhombus(n):
    for i in range(n):
        print(" "*(n-i-1)+"*",end="")
        if i==0:
            print("")
        else:
            print(" " *(2*i-1)+"*")
    for i in range(n-2,-1,-1):
        print(" " * (n - i - 1) + "*", end="")
        if i == 0:
            print("")
        else:
            print(" " * (2 * i - 1) + "*")



hollowRhombus(5)
#pattern1and2(5)
#pattern3(5)
