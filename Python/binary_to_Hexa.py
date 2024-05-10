def print_formatted(number):
    # your code goes here
#    l=int(len(bin(n+1)))
    for i in range(1,n+1):
        l = len("{0:b}".format(number))
        b=bin(i)[2:]
        o=oct(i)[2:]
        h=hex(i)[2:]
        print("{:>5} {:>5} {:>5} {:>5}".format(i, o, h, b))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

