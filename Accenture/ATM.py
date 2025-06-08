"""
n=10 #int(input(" Enter N: "))
amount=1300 #int(input("Enter Amount : "))
hundred= 10 #int(input("Enter number of hundred Notes : "))
twohundred=10 #int(input("Enter 200 : "))
fivehundred=10 #int(input("Enter 500 : "))
thousand=10 #int(input("Enter 1000 : "))

sum=0
for i in range(hundred):
    sum=sum+i*100
    if sum<amount:
        print(sum)

"""


def main():
    sum1 = sum2 = sum3 = 0
    co = 0
    n = int(input())
    max_value = int(input())
    h = int(input())
    tw = int(input())
    f = int(input())
    th = int(input())

    for i in range(h + 1):
        sum1 = i * 100
        if sum1 == max_value and i <= n and i > co:
            co = i
        if sum1 < max_value:
            for j in range(tw + 1):
                sum2 = sum1 + j * 200
                if sum2 == max_value and (i + j) <= n and (j + i) > co:
                    co = j + i
                if sum2 < max_value:
                    for k in range(f + 1):
                        sum3 = sum2 + k * 500
                        if sum3 == max_value and (i + j + k) <= n and (i + j + k) > co:
                            co = i + j + k
                        if sum3 < max_value:
                            for l in range(th + 1):
                                sum4 = sum3 + l * 1000
                                if sum4 == max_value and (i + j + k + l) <= n and (i + j + k + l) > co:
                                    co = i + j + k + l
                                if sum4 > max_value:
                                    break

    print(co)


if __name__ == "__main__":
    main()

