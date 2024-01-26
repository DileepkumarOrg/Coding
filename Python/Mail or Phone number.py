import time
mail=input("Enter mail or Phone number")
var="dileepkumar"
if(mail in var or mail==8179724985):
    print("OTP is Send successfully")
    otp=int(input("Enter OTP"))
    if(otp==1234):
        print("Link is shared to your mobile number")
    else:
        print("Wrong otp")
else:
    print("No user with this phone number or Mail ID")
    time.sleep(2)
    print("Please try again later")
