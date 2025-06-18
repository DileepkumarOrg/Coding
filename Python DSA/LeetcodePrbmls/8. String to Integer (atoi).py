def myAtoi(x):
    x = "    35"
    x = x.strip(" ")
    res = ""
    if not x:
        return 0
    sign =1
    i = 0
    if x[0] == "-":
        sign = -1
        i += 1
    else:
        return
    for j in range(i,len(x)):
        if x[i].isdigit():
            res += x[i]
        else :
            return int(res)
    return int(res)
print(myAtoi("1337c0d3"))


s = "2345"
j=0
for i in s:
    res = ord(i)-ord("0")
    j += 1
    print(res)

re = ["Ani papa plz pettu raa ....!    " for i in range(100)]
print(*re)
