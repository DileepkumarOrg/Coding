def prime(num):
    for i in range(2,num):
        if (num==0 | num==1):
            print("It is not a prime number. ")
        elif(num% i !=0):
            print("It is  a prime number. ")
        else:
            print("It is not a primr number. ")


prime(8)