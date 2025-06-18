x = -135
def rev(s):
    return s[::-1]
res = rev(str(x))
print((int(res[0:-1])*-1 if int(res[0:-1])*-1 > -2147483648 else 0 ) if x<0 else (int(res) if int(res) < 2147483647 else 0))
