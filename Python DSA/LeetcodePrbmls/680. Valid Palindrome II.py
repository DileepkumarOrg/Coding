"""def validPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        for i in range(len(s)):
            d = s
            d = d[0:i] + d[i + 1:len(d)]
            if d == d[::-1]:
                return True
    return False"""


def validPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        l,r,c = 0,len(s)-1, 0
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l+1:r+1] == s[l+1:r+1][::-1] and len(s[l+1:r+1]) > 2:
                    return True
                elif s[l+1:r-1] == s[l+1:r-1][::-1] and len(s[l+1:r-1]) > 2:
                    return True
                else:
                    l += 1
                    r -= 1


    return False

s = "abca"
print(validPalindrome(s))

