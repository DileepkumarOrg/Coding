#Online payment for any online shopping Application
import time
print("1.UPI\n2.Net Bnaking\n3.CreditCard Debitcard Or AtmCard")
Choice=int(input("Select your Payment Method    "))
if(Choice==1):    #UPI
    print("1.Phone Pay\n2.Paytm\n3.Amazon Pay")
    Chance=int(input("Select your UPI Method  "))
    time.sleep(2)
    if(Chance==1):
        print("Your payment is redirecting to Phone pay")
        time.sleep(1)
        print("Your order placed")
    elif(Chance==2):
        print("Your payment is Redirecting to Paytm")
        time.sleep(1)
        print("Your order placed")
    elif(Chance==3):
        print("Your payment is Redirecting to Amazon Pay")
        time.sleep(1)
        print("Your order placed")
    else:
        print("Error Try again")
elif(Choice==2):   #Net banking
    print("1.State Bank of India\n2.ICICI Bank")
    Chance2=int(input("Select your choice  "))
    time.sleep(2)
    if(Chance2==1):
        print("Welcome to SBI")
        username=str(input("Enter User name  "))
        password=str(input("Enter Your password  "))
        time.sleep(2)
        if username == 'kiran' and password == 'gurucharan':
            print("Username and password verify successfully ")
            time.sleep(1)
            OTP2 = int(input("Enter One Time Password Already sent to your Registered mobile number  "))
            if(OTP2==1234):
                print("Please wait do not cancel or refresh page during processing")
                time.sleep(1)
                print("Your OTP verified Successfully")
                time.sleep(1)
                print("your order Placed")
            else:
                print("Wrong OTP ")
                time.sleep(1)
                print("Please Try again")
        else:
            print("Entered Username and Pass word not matched")
    elif(Chance2==2):
        print("Welcome to ICICI Bank")
        username = str(input("Enter User name  "))
        password = str(input("Enter Your password  "))
        time.sleep(2)
        if username == 'kiran' and password == 'gurucharan':
            print("Username and password verify successfully ")
            time.sleep(1)
            OTP2 = int(input("Enter One Time Password Already sent to your Registered mobile number  "))
            if (OTP2 == 1234):
                print("Please wait do not cancel or refresh page during processing")
                time.sleep(1)
                print("Your OTP verified Successfully")
                time.sleep(1)
                print("your order Placed")
            else:
                print("Wrong OTP ")
                time.sleep(1)
                print("Please Try again")
        else:
            print("Entered Username and Pass word not matched")
    else:
        print("Invalid selection")
elif(Choice==3):
    card_num = (int(input("Enter your Card number  ")))
    time.sleep(2)
    OTP = int(input("Enter One Time Password Already sent to your Registered mobile number  "))
    if card_num==1234567890 and OTP==1234:
        print("Please wait do not cancel or refresh page during processing")
        time.sleep(2)
        print("Verified successfully")
        time.sleep(1)
        print("Your order placed")
    else:
        print("Card number number is invalid")
        time.sleep(1)
        print("Contact near Branch")
else:
    print("Invalid Choice")
    time.sleep(1)
    print("Please try again")