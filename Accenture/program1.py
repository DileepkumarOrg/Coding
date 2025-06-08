"""Character Count

You are given a string S of length N. Your friend wants to know the
number of times his favorite letter C occurs in the string. Your task, is
to help your friend find and retum an integer value representing the
number of times a character occurs in a particular string.  """

def count(s,n,c):
    return s.count(c)
s=input("")
n=int(input(""))
c=input("")
print(count(s,n,c))