strs = ["flower","flow","flight"]
strs.sort()
pre = ""
for i in range(len(sorted(strs , key= lambda x : len(x))[0])):
    if strs[0][i] == strs[-1][i]:
        pre += strs[0][i]
    else:
        break
print(pre)